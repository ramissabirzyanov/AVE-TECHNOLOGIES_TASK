from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    REDISHOST: str
    REDISPORT: int
    DB: int
    DECODE: bool

    model_config = ConfigDict(
        env_file=".env",
        extra="allow"
    )


settings = Settings()
