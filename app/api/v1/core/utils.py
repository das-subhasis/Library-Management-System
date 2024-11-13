from datetime import datetime, date, timedelta
from fastapi import FastAPI
from app.api.v1.db import Settings
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await Settings.initialize_db()
    yield
    print('api is shutting down....')

def calculate_expiration_date(current_date: date):
    return current_date + timedelta(days=365)

