from sqlalchemy import Column, BigInteger, String, Text, TIMESTAMP, Enum, ForeignKey, func
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

import enum


class ChatScope(str, enum.Enum):
    LESSON = "LESSON"
    COURSE = "COURSE"
    PROGRAM = "PROGRAM"
    SUPPORT = "SUPPORT"


class ChatChannel(Base):
    __tablename__ = "chat_channels"

    channel_id = Column(BigInteger, primary_key=True, autoincrement=True)
    scope_type = Column(Enum(ChatScope), nullable=False)  # which entity (lesson, course, etc.)
    scope_id = Column(BigInteger, nullable=False)         # the ID of that entity
    created_by = Column(BigInteger, ForeignKey("users.user_id"))
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

    creator = relationship("User", back_populates="chat_channels_created")
    messages = relationship("ChatMessage", back_populates="channel")


class ChatMessage(Base):
    __tablename__ = "chat_messages"

    message_id = Column(BigInteger, primary_key=True, autoincrement=True)
    channel_id = Column(BigInteger, ForeignKey("chat_channels.channel_id"), nullable=False)
    user_id = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    message = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

    channel = relationship("ChatChannel", back_populates="messages")
    user = relationship("User", back_populates="chat_messages")
