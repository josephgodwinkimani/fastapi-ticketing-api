# app/main.py
from fastapi import FastAPI
from app.api import routes
from app.logging_config import setup_logging
from app.database import db

setup_logging()

app = FastAPI()

@app.on_event("startup")
async def startup():
    await db.connect()

@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()

app.include_router(routes.router)