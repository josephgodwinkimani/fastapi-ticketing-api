# app/schemas.py
from pydantic import BaseModel, EmailStr
from typing import List, Optional


class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    tickets: Optional[List[int]] = []

    class Config:
        orm_mode = True


class TicketBase(BaseModel):
    title: str
    description: str
    priority: str
    category: str
    userId: int


class TicketCreate(TicketBase):
    pass


class Ticket(TicketBase):
    id: int
    status: str
    replies: Optional[List[int]] = []

    class Config:
        orm_mode = True


class ReplyBase(BaseModel):
    content: str


class ReplyCreate(ReplyBase):
    pass
