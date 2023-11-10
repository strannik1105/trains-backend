from fastapi_jwt_auth import AuthJWT

from models.users import User
from fastapi import Request, Response
from user_agents import parse


def verify_password(password: str, user_obj: User) -> bool:
    if user_obj.password == password:
        return True
    else:
        return False


def user_agent_parser(user_agent: str, request: Request):
    """
    Вспомогательная функция для получения устройства, ос пользователя и ip.
    :param user_agent: данные из user-agent
    :param request: данные из запроса
    """
    ip_address = request.scope.get("root_path")
    agent_from_user = f'{request.headers.get("Agent", "")}/ '
    platform_from_user = f'{request.headers.get("platform", "")}/ '
    user_agent_data = parse(user_agent)
    agent = (
        f"{agent_from_user}{user_agent_data.browser[0]}" f"{user_agent_data.browser[2]}"
    )
    platform = (
        f"{platform_from_user}{user_agent_data.device[0]}",
        f" {user_agent_data.os[0]}{user_agent_data.os[2]}",
    )
    return agent, platform, ip_address


def remove_cookie(
        jwt_service: AuthJWT,
        response: Response,
        cookie_key: str,
        cookie_path: str,
        http_only: bool = True,
):
    """
    Additional function for token removal from cookie
    :param jwt_service: (library for cookies settings)
    :param response: response object, when we need to delete cookies
    :param cookie_key: cookie_key
    :param cookie_path: cookie_path
    :param http_only: httpOnly cookies flag
    :return:
    """
    response.set_cookie(
        cookie_key,
        "",
        max_age=0,
        path=cookie_path,
        domain=jwt_service._cookie_domain,
        secure=jwt_service._cookie_secure,
        httponly=http_only,
        samesite=jwt_service._cookie_samesite,
    )
    return response
