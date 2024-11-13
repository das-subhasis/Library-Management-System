from fastapi import FastAPI
from Backend.app.api.v1.core import lifespan
from Backend.app.api.v1 import routes

app = FastAPI(
    title="Library Management API (ver. 1.0)",
    lifespan=lifespan
)

############################################################
app.include_router(routes.LibraryRoute)
app.include_router(routes.AdminRoute)
############################################################


@app.get('/')
def home():
    return {'message': 'Welcome to Library Management API (ver. 1.0), created by Subhasis Das.'}



