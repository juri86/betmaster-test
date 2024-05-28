from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    HEADLESS: bool = False
    BLINK_ELEMENT: bool = True
    ELEMENT_TIMEOUT: int = 10000
    SLOW_MO: int = 100


@lru_cache()
def settings():
    return Settings()


class Env:
    production_host = "https://betmaster.ee/en/casino/slots"
    wiremock_host = "http://localhost:8888"     # wiremock