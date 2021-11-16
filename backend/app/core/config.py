from starlette.config import Config
from starlette.datastructures import Secret


config = Config(".env")

SECRET_KEY = config("SECRET_KEY", cast=Secret, default="CHANGEME")

POSTGRES_USER = config("POSTGRES_USER", cast=str)
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=Secret)
POSTGRES_HOST = config("POSTGRES_HOST", cast=str)
POSTGRES_PORT = config("POSTGRES_PORT", cast=str, default="5432")
POSTGRES_DB = config("POSTGRES_DB", cast=str)

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

IPFS_ADDRESS = config("IPFS_ADDRESS", cast=str)
IPFS_PORT = config("IPFS_PORT", cast=int, default=5001)