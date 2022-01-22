from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "provider"
    app_server: str = "http://localhost:8000"