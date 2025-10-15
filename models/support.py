from sqlalchemy import Column, BigInteger, String, Text, TIMESTAMP, Enum, ForeignKey, func
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

import enum


class TicketStatus(str, enum.Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    RESOLVED = "RESOLVED"
    CLOSED = "CLOSED"


class TicketPriority(str, enum.Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    URGENT = "URGENT"


class SupportTicket(Base):
    __tablename__ = "support_tickets"

    ticket_id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    subject = Column(String(255), nullable=False)
    status = Column(Enum(TicketStatus), default=TicketStatus.OPEN, nullable=False)
    priority = Column(Enum(TicketPriority), default=TicketPriority.MEDIUM, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    user = relationship("User", back_populates="support_tickets")
    messages = relationship("SupportMessage", back_populates="ticket")


class SupportMessage(Base):
    __tablename__ = "support_messages"

    support_message_id = Column(BigInteger, primary_key=True, autoincrement=True)
    ticket_id = Column(BigInteger, ForeignKey("support_tickets.ticket_id"), nullable=False)
    sender_id = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    message = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

    ticket = relationship("SupportTicket", back_populates="messages")
    sender = relationship("User", back_populates="support_messages")
