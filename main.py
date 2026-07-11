# FastAPI
from fastapi import FastAPI

# Database
from database.base import Base
from db import engine

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


# Endpoint: / - Method: GET
@app.get("/")
async def root():
    return {"message": "Server is functioning"}


# Endpoint: /api - Method: GET
@app.get("/api")
async def api():
    return {"message": "Welcome to Mahi Todo List API"}
