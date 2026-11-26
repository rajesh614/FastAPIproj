import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=env_path)


def required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"{name} is missing from {env_path}")
    return value


class Settings:
    PROJECT_TITLE: str = "Blog"
    PROJECT_VERSION: str = "0.1.0"

    POSTGRES_USER: str = required_env("POSTGRES_USER")
    POSTGRES_PASSWORD: str = required_env("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = required_env("POSTGRES_SERVER")
    POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT", "5432"))
    POSTGRES_DB: str = required_env("POSTGRES_DB")


settings = Settings()
