from enum import Enum

from pydantic import BaseModel


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
    title: str
    description: str
    priority: TicketPriority
    category: str


class TicketUpdate(BaseModel):
    title: str
    description: str
    priority: TicketPriority
    category: str
    status: TicketStatus