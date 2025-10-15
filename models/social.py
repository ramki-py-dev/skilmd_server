from sqlalchemy import Column, BigInteger, String, Text, TIMESTAMP, ForeignKey, Enum, Boolean, func, CHAR
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

import enum


class InvitationStatus(str, enum.Enum):
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    DECLINED = "DECLINED"
    EXPIRED = "EXPIRED"


class CourseInvitation(Base):
    __tablename__ = "course_invitations"

    invitation_id = Column(BigInteger, primary_key=True, autoincrement=True)
    course_id = Column(BigInteger, ForeignKey("courses.course_id"), nullable=False)
    inviter_id = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    invitee_email = Column(String(255), nullable=False)
    token = Column(CHAR(36), unique=True, nullable=False)
    status = Column(Enum(InvitationStatus), default=InvitationStatus.PENDING, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    accepted_at = Column(TIMESTAMP)

    course = relationship("Course", back_populates="invitations")
    inviter = relationship("User", back_populates="sent_invitations")


class UserGroup(Base):
    __tablename__ = "user_groups"

    group_id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    created_by = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    is_private = Column(Boolean, default=False, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

    creator = relationship("User", back_populates="groups_created")
    members = relationship("GroupMember", back_populates="group")
    invitations = relationship("GroupInvitation", back_populates="group")


class GroupRole(str, enum.Enum):
    OWNER = "OWNER"
    MODERATOR = "MODERATOR"
    MEMBER = "MEMBER"


class GroupMember(Base):
    __tablename__ = "group_members"

    group_id = Column(BigInteger, ForeignKey("user_groups.group_id"), primary_key=True)
    user_id = Column(BigInteger, ForeignKey("users.user_id"), primary_key=True)
    role = Column(Enum(GroupRole), default=GroupRole.MEMBER, nullable=False)
    joined_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

    group = relationship("UserGroup", back_populates="members")
    user = relationship("User", back_populates="group_memberships")


class GroupInvitation(Base):
    __tablename__ = "group_invitations"

    group_invitation_id = Column(BigInteger, primary_key=True, autoincrement=True)
    group_id = Column(BigInteger, ForeignKey("user_groups.group_id"), nullable=False)
    inviter_id = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    invitee_email = Column(String(255), nullable=False)
    token = Column(CHAR(36), unique=True, nullable=False)
    status = Column(Enum(InvitationStatus), default=InvitationStatus.PENDING, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

    group = relationship("UserGroup", back_populates="invitations")
    inviter = relationship("User", back_populates="group_invitations_sent")
