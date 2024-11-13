from datetime import date, timedelta
from fastapi import FastAPI
from Backend.app.api.v1.db import Settings
from contextlib import asynccontextmanager
import random


@asynccontextmanager
async def lifespan(app: FastAPI):
    await Settings.initialize_db()
    yield
    print('api is shutting down....')


def calculate_expiration_date(current_date: date):
    return current_date + timedelta(days=365)


def generate_id():
    return random.randint(10**12, 10**13 - 1)
