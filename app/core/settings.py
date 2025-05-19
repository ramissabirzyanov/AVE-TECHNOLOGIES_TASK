from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    class Config:
        extra = "allow"


settings = Settings()
