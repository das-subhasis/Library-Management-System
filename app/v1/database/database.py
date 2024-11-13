from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import DatabaseError
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from utils.config import Config
# from utils.exceptions import DBExceptions
from typing import Annotated


class Settings:
    SQLALCHEMY_DATABASE_URL = Config.SQL_ALCHEMY_DATABASE_URL

    engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

    AsyncSessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine, class_=AsyncSession)

    BASE = declarative_base()

    @staticmethod
    async def get_async_db():
        async with Settings.AsyncSessionLocal() as db:
            yield db

    @staticmethod
    async def initialize_db():
        try:
            async with Settings.engine.begin() as conn:
                await conn.run_sync(Settings.BASE.metadata.create_all)
                print("Tables have been created successfully.")
        except Exception as e:
            return e


DB_Session = Annotated[AsyncSession, Depends(Settings.get_async_db)]