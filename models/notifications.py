from sqlalchemy import Column, BigInteger, String, Text, TIMESTAMP, Boolean, ForeignKey, JSON, func
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Notification(Base):
    __tablename__ = "notifications"

    notification_id = Column(BigInteger, primary_key=True, autoincrement=True)
    type = Column(String(50), nullable=False)  # e.g., ANNOUNCEMENT, QUIZ_RESULT
    title = Column(String(255), nullable=False)
    body = Column(Text)
    metadata = Column(JSON)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

    deliveries = relationship("UserNotification", back_populates="notification")


class UserNotification(Base):
    __tablename__ = "user_notifications"

    user_notification_id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    notification_id = Column(BigInteger, ForeignKey("notifications.notification_id"), nullable=False)
    is_read = Column(Boolean, default=False, nullable=False)
    delivered_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    read_at = Column(TIMESTAMP)

    user = relationship("User", back_populates="notifications")
    notification = relationship("Notification", back_populates="deliveries")
