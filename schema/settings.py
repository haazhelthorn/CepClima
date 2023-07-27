from pydantic import BaseConfig


class Settings(BaseConfig):
    app_name: str = "Curso FastApi"
    admin_email = str
    items_per_user = int = 50
    idapi = str

    class Config:
        env_file = ".env"
