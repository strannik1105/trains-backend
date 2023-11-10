from common.schemas.base import PydanticBase


class Msg(PydanticBase):
    msg: str


class MsgLogin(PydanticBase):
    msg: str
    agent: str
    platform: list
