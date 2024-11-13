from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from Backend.api.v1.core import Config
from typing import Annotated


class Settings:
    SQLALCHEMY_DATABASE_URL = Config.SQL_ALCHEMY_DATABASE_URL

    engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

    AsyncSessionLocal = async_sessionmaker(autoflush=False, autocommit=False, bind=engine)

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