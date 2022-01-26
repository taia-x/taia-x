from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "provider"
    app_server: str = "http://0.0.0.0:8000"