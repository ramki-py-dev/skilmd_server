from sqlalchemy import Column, String, BigInteger, Text, Boolean, TIMESTAMP, func
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True, autoincrement=True)
    email = Column(String(255), nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(150), nullable=False)
    phone = Column(String(30), nullable=True)
    bio = Column(Text, nullable=True)
    avatar_url = Column(String(500), nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    roles = relationship("UserRole", back_populates="user")
    enrollments = relationship("Enrollment", back_populates="user")
    reviews = relationship("CourseReview", back_populates="user")
    program_enrollments = relationship("ProgramEnrollment", back_populates="user")
    organizations = relationship("OrganizationUser", back_populates="user")
    sent_invitations = relationship("CourseInvitation", back_populates="inviter")
    groups_created = relationship("UserGroup", back_populates="creator")
    group_memberships = relationship("GroupMember", back_populates="user")
    group_invitations_sent = relationship("GroupInvitation", back_populates="inviter")
    notifications = relationship("UserNotification", back_populates="user")
    chat_channels_created = relationship("ChatChannel", back_populates="creator")
    chat_messages = relationship("ChatMessage", back_populates="user")
    support_tickets = relationship("SupportTicket", back_populates="user")
    support_messages = relationship("SupportMessage", back_populates="sender")
    instructed_courses = relationship("CourseInstructor", back_populates="user")



