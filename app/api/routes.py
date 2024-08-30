# app/api/routes.py
from fastapi import APIRouter, Depends, HTTPException
from app import crud, schemas

router = APIRouter()

@router.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate):
    try:
        return await crud.create_user(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/tickets/", response_model=schemas.Ticket)
async def create_ticket(ticket: schemas.TicketCreate):
    try:
        return await crud.create_ticket(ticket)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/tickets/{ticket_id}/reply/", response_model=schemas.ReplyBase)
async def add_reply(ticket_id: int, reply: schemas.ReplyCreate):
    try:
        return await crud.add_reply(ticket_id, reply)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/tickets/{ticket_id}/close/", response_model=schemas.Ticket)
async def close_ticket(ticket_id: int):
    ticket = await crud.close_ticket(ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

@router.get("/tickets/", response_model=list[schemas.Ticket])
async def get_tickets():
    try:
        return await crud.get_all_tickets()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/users/{user_id}/tickets/", response_model=list[schemas.Ticket])
async def get_user_tickets(user_id: int):
    try:
        return await crud.get_user_tickets(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))