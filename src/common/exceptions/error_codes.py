from enum import Enum


class ErrorCodes(Enum):
    """
    Ошибка в формате: имя = (код, HTTP код, описание)
    """

    incorrect_credentials = (0, 401, "неверные учётные данные")
