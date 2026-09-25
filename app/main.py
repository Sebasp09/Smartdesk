from fastapi import FastAPI

from app.database import Base, engine
from app.routers import tickets

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tickets.router)


@app.get("/")
def home():
    return {
        "message": "SmartDesk API funcionando"
    }