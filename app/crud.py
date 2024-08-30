# app/crud.py
from app.database import db
from . import schemas
import logging

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


async def create_user(user: schemas.UserCreate):
    logger.info(f"Creating user: {user}")
    db_user = await db.user.create(
        data={
            "name": user.name,
            "email": user.email,
        }
    )
    logger.info(db_user)
    return db_user


async def create_ticket(ticket: schemas.TicketCreate):
    logger.info(f"Creating ticket: {ticket}")
    db_ticket = await db.ticket.create(
        data={
            "title": ticket.title,
            "description": ticket.description,
            "priority": ticket.priority,
            "category": ticket.category,
            "userId": ticket.userId,
        }
    )
    return db_ticket


async def add_reply(ticket_id: int, reply: schemas.ReplyCreate):
    logger.info(f"Creating ticket reply: {reply} for ticket id #{ticket_id}")
    db_reply = await db.reply.create(
        data={
            "ticketId": ticket_id,
            "content": reply.content,
        }
    )
    return db_reply


async def close_ticket(ticket_id: int):
    logger.info(f"Closing ticket id: {ticket_id}")
    ticket = await db.ticket.update(
        where={"id": ticket_id},
        data={"status": "closed"}
    )
    return ticket


async def get_all_tickets():
    return await db.ticket.find_many(include={"replies": True, "user": True})


async def get_user_tickets(user_id: int):
    return await db.ticket.find_many(where={"userId": user_id}, include={"replies": True})
