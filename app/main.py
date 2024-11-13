from fastapi import FastAPI
from app.api.v1.core import lifespan
from app.api.v1.routes import LibraryRoute

app = FastAPI(
    title="Library Management API (ver. 1.0)",
    lifespan=lifespan
)

############################################################
app.include_router(LibraryRoute)
############################################################


@app.get('/')
def home():
    return {'message': 'Welcome to Library Management API (ver. 1.0), created by Subhasis Das.'}



