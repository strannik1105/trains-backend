import os
from datetime import timedelta

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv(os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)), ".env"))

HOST = os.getenv("HOST", "0.0.0.0")
PORT: int = int(os.getenv("PORT", 8000))

ON_PRODUCTION: bool = False
SECRET_KEY = "secret"

POSTGRES_DB: str = os.getenv("POSTGRES_DB", "trains")
POSTGRES_USER: str = os.getenv("POSTGRES_USER", "user")
POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "password")
POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "0.0.0.0")
POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT", "5432"))

REDIS_HOST: str = os.getenv("REDIS_HOST", "0.0.0.0")
REDIS_PORT: int = int(os.getenv("REDIS_PORT", "6379"))

CLICKHOUSE_DB: str = os.getenv("CLICKHOUSE_DB", "trains")
CLICKHOUSE_USER: str = os.getenv("CLICKHOUSE_USER", "user")
CLICKHOUSE_PASSWORD: str = os.getenv("CLICKHOUSE_PASSWORD", "password")
CLICKHOUSE_HOST: str = os.getenv("CLICKHOUSE_HOST", "0.0.0.0")
CLICKHOUSE_PORT: int = int(os.getenv("CLICKHOUSE_PORT", "9000"))

RABBITMQ_HOST: str = os.getenv("RABBITMQ_HOST", "0.0.0.0")
RABBITMQ_PORT: str = os.getenv("RABBITMQ_PORT", "5672")
RABBITMQ_USER: str = os.getenv("RABBITMQ_USER", "guest")
RABBITMQ_PASSWORD: str = os.getenv("RABBITMQ_PASSWORD", "guest")
RABBITMQ_PARSER_EXCHANGE: str = os.getenv("RABBITMQ_PARSER_EXCHANGE", "parser_output_exchange")


class CookiesSettings(BaseSettings):
    # Configure application to store and get JWT from cookies
    authjwt_token_location: set = {"cookies"}
    authjwt_algorithm: str = "HS256"

    authjwt_secret_key: str = SECRET_KEY

    auth_access_token_lifetime: int = timedelta(minutes=30).total_seconds()
    auth_refresh_token_lifetime: int = timedelta(days=15).total_seconds()

    access_expires: int = timedelta(minutes=30).total_seconds()
    refresh_expires: int = timedelta(days=15).total_seconds()

    authjwt_access_token_expires: int = timedelta(minutes=30).total_seconds()
    authjwt_refresh_token_expires: int = timedelta(days=15).total_seconds()

    authjwt_cookie_secure: bool = ON_PRODUCTION
    authjwt_cookie_csrf_protect: bool = False

    authjwt_cookie_samesite: str = "none"  # noqa

    authjwt_denylist_enabled = False
    # authjwt_denylist_token_checks: set = {"access", "refresh"}


cookies_settings = CookiesSettings()
