from typing import Any

from fastapi import APIRouter, Request, Depends, Header, Query
from fastapi_jwt_auth import AuthJWT
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status
from starlette.responses import JSONResponse

from common.db.session import redis_client
from common.exceptions.error_codes import ErrorCodes
from common.exceptions.exceptions import BackendException
from common.schemas.messages import Msg, MsgLogin
from models.users.repository.user import user_repository
from router import deps
from router.v1.authentication.ext import user_agent_parser, remove_cookie
from settings import cookies_settings

router = APIRouter()


@router.post("/login", response_model=MsgLogin)
async def login(
        db: deps.PGSession,
        request: Request,
        form_data: OAuth2PasswordRequestForm = Depends(),
        Authorize: AuthJWT = Depends(),
        user_agent: str = Header(None),
) -> Any:
    user = await user_repository.authenticate(
        db, email=form_data.username.lower(), password=form_data.password
    )
    if not user:
        raise BackendException(error=ErrorCodes.incorrect_credentials)

    payload = {
        'sid': str(user.sid),
    }
    # access_token = Authorize.create_access_token(subject=json.dumps(payload))
    # refresh_token = Authorize.create_refresh_token(subject=json.dumps(payload))
    access_token = Authorize.create_access_token(
        subject=str(user.sid), user_claims=payload
    )
    refresh_token = Authorize.create_refresh_token(
        subject=str(user.sid), user_claims=payload
    )

    agent, platform, ip_login = user_agent_parser(user_agent, request)

    await db.commit()

    response = {
        "msg": "Success Logins!",
        "agent": agent,
        "platform": platform,
        "ip": ip_login,
    }

    response = JSONResponse(response, status_code=status.HTTP_200_OK)

    Authorize.set_access_cookies(
        access_token, response, max_age=cookies_settings.auth_access_token_lifetime
    )
    Authorize.set_refresh_cookies(
        refresh_token, response, max_age=cookies_settings.auth_refresh_token_lifetime
    )

    redis_client.setex(
        f"{user.sid}:{Authorize.get_jti(access_token)}",
        cookies_settings.access_expires,
        "False",
    )
    redis_client.setex(
        f"{user.sid}:{Authorize.get_jti(refresh_token)}",
        cookies_settings.refresh_expires,
        "False",
    )

    return response


@router.post("/refresh_token", response_model=Msg)
async def update_access_token(
        Authorize: AuthJWT = Depends(),
) -> Any:
    Authorize.jwt_refresh_token_required()

    user_sid = Authorize.get_jwt_subject()
    perms = Authorize.get_raw_jwt()["permissions"]

    updated_access_token = Authorize.create_access_token(
        subject=user_sid, user_claims={"permissions": perms}
    )
    updated_refresh_token = Authorize.create_refresh_token(
        subject=user_sid, user_claims={"permissions": perms}
    )

    response = JSONResponse(
        {"msg": "Success tokens renewal"}, status_code=status.HTTP_200_OK
    )
    Authorize.set_access_cookies(
        updated_access_token,
        response,
        max_age=cookies_settings.auth_access_token_lifetime,
    )
    Authorize.set_refresh_cookies(
        updated_refresh_token,
        response,
        max_age=cookies_settings.auth_refresh_token_lifetime,
    )

    redis_client.setex(
        f'{user_sid}:{Authorize.get_raw_jwt()["jti"]}',
        cookies_settings.access_expires,
        "True",
    )

    return response


@router.post("/logout", response_model=Msg)
async def logout(
        Authorize: AuthJWT = Depends(),
        everywhere: bool = Query(False, description="Выйти со всех устройств"),
):
    Authorize.jwt_required()
    res = JSONResponse({"msg": "Successfully logout"}, status_code=status.HTTP_200_OK)

    remove_cookie(
        Authorize, res, Authorize._access_cookie_key, Authorize._access_cookie_path
    )
    remove_cookie(
        Authorize, res, Authorize._refresh_cookie_key, Authorize._refresh_cookie_path
    )

    if everywhere:
        redis_client.setex(
            Authorize.get_jwt_subject(), cookies_settings.refresh_expires, "*"
        )
        keys = redis_client.keys(f"{Authorize.get_jwt_subject()}:*")
        for key in keys:
            redis_client.set(key, "True", keepttl=True)
    else:
        jti_access = Authorize.get_raw_jwt()["jti"]
        redis_client.setex(
            f"{Authorize.get_jwt_subject()}:{jti_access}",
            cookies_settings.access_expires,
            "True",
        )
    return res
