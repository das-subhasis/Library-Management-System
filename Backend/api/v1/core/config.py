from dotenv import load_dotenv
import os

load_dotenv()


class Config:

    SQL_ALCHEMY_DATABASE_URL = os.getenv("SQL_ALCHEMY_DATABASE_URL")
    PYENV = os.getenv("PYENV")
    SECRET_KEY = os.getenv("SECRET_KEY")
    REDIS_PORT = os.getenv("REDIS_PORT")
    CACHE_EXPIRY_MINUTES = os.getenv("CACHE_EXPIRY_MINUTES")
    USER_TOKEN_EXPIRY_MINUTES = os.getenv("USER_TOKEN_EXPIRY_MINUTES")
    LIBRARIAN_TOKEN_EXPIRY_MINUTES = os.getenv("LIBRARIAN_TOKEN_EXPIRY_MINUTES")
