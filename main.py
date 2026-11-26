import logging

from fastapi import FastAPI
from core.config import settings
from db.session import engine, check_database_connection
from db.base_class import Base

logging.basicConfig(level=logging.INFO)

def create_tables():
    Base.metadata.create_all(bind=engine)
    
def start_app():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    if check_database_connection():
        create_tables()
    else:
        logging.getLogger(__name__).error("Skipping table creation because the database is unavailable")
    return app

app = start_app()

@app.get("/")
def name() -> dict[str, str]:
    return {"msg": "Hello FastAPI"}
