from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate, TicketUpdate

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "SmartDesk API funcionando"}


@app.post("/tickets")
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    new_ticket = Ticket(
        title=ticket.title,
        description=ticket.description,
        priority=ticket.priority,
        category=ticket.category
    )

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    return {
        "message": "Ticket creado correctamente",
        "ticket": new_ticket
    }
    
@app.get("/tickets")
def get_tickets(db: Session = Depends(get_db)):
    tickets = db.query(Ticket).all()

    return {
        "tickets": tickets
    }
    
@app.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket no encontrado"
        )

    return {
        "ticket": ticket
    }
    

@app.put("/tickets/{ticket_id}")
def update_ticket(
    ticket_id: int,
    ticket_data: TicketUpdate,
    db: Session = Depends(get_db)
):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket no encontrado"
        )

    ticket.title = ticket_data.title
    ticket.description = ticket_data.description
    ticket.priority = ticket_data.priority
    ticket.category = ticket_data.category

    db.commit()
    db.refresh(ticket)

    return {
        "message": "Ticket actualizado correctamente",
        "ticket": ticket
    }


@app.delete("/tickets/{ticket_id}")
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket no encontrado"
        )

    db.delete(ticket)
    db.commit()

    return {
        "message": "Ticket eliminado correctamente"
    }