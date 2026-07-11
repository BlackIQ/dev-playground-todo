# FastAPI
from fastapi import FastAPI

# Database
from database.base import Base
from db import engine

# Routes
from routers import (
    task
)

# Import all of Models
import models

# Create tables
Base.metadata.create_all(bind=engine)

# Create FastAPI instance
app = FastAPI(
    title="Mahi Todo List API",
    version="1.0.0",
    summary="A simple Backend as out first project to use APIs in ReactJs",
    description="",
    openapi_tags=[
        {"name": "Application", "description": "Application endpoints like root and ping"},
        {"name": "Task", "description": "Task endpoints having all HTTP methods"}
    ]
)


@app.get("/", tags=["Application"])
async def root():
    """
    A simple route just to check server is running

    - Endpoint: /
    - Method: GET
    """

    return {"message": "Server is functioning"}


@app.get("/api", tags=["Application"])
async def api():
    """
    Where the whole application begins from

    - Endpoint: /api
    - Method: GET
    """

    return {"message": "Welcome to Mahi Todo List API"}


# Task router
app.include_router(task.router, prefix="/api")
