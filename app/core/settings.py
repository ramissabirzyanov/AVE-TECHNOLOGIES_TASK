from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    REDISHOST: str
    REDISPORT: int
    DB: int
    DECODE: bool

    class Config:
        extra = "allow"
        env_file = ".env"


settings = Settings()
