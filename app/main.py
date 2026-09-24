from fastapi import FastAPI
from app.schemas.ticket import TicketCreate

app = FastAPI()

@app.get("/")
def home():
    return {"message": "SmartDesk APII funcionando"}

@app.post("/tickets")
def create_ticket(ticket: TicketCreate):
    return {"message": "Ticket creado correctamente",
            "ticket": ticket
            }
    