from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class TicketPriority(str, Enum):
    BAJA = "Baja"
    MEDIA = "Media"
    ALTA = "Alta"
    CRITICA = "Crítica"


class TicketStatus(str, Enum):
    ABIERTO = "Abierto"
    EN_PROGRESO = "En progreso"
    RESUELTO = "Resuelto"
    CERRADO = "Cerrado"


class TicketCreate(BaseModel):
    title: str = Field(
        min_length=5,
        max_length=150
    )

    description: str = Field(
        min_length=10
    )

    priority: TicketPriority

    category: str = Field(
        min_length=3,
        max_length=50
    )


class TicketUpdate(BaseModel):
    title: str = Field(
        min_length=5,
        max_length=150
    )

    description: str = Field(
        min_length=10
    )

    priority: TicketPriority

    category: str = Field(
        min_length=3,
        max_length=50
    )

    status: TicketStatus


class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: TicketPriority
    category: str
    status: TicketStatus
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }