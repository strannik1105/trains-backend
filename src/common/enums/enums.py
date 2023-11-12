from enum import StrEnum, auto


class Role(StrEnum):
    SUPERUSER = auto()
    ADMIN = auto()
    MEMBER = auto()
