from datetime import date, timedelta
from fastapi import FastAPI
from Backend.api.v1.db import Settings
from contextlib import asynccontextmanager
from typing import List
import random


@asynccontextmanager
async def lifespan(app: FastAPI):
    await Settings.initialize_db()
    yield
    print('api is shutting down....')


def calculate_expiration_date(current_date: date):
    return current_date + timedelta(days=365)


def generate_id():
    return random.randint(10 ** 12, 10 ** 13 - 1)


def generate_batch(data: List, batch_size: int = 5):
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]
