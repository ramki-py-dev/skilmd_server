from sqlalchemy import Column, String, BigInteger, Enum, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

import enum


class OrgType(str, enum.Enum):
    HOSPITAL = "HOSPITAL"
    UNIVERSITY = "UNIVERSITY"
    DEVICE_COMPANY = "DEVICE_COMPANY"
    OTHER = "OTHER"


class Organization(Base):
    __tablename__ = "organizations"

    organization_id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    org_type = Column(Enum(OrgType), nullable=False)
    website = Column(String(255))
    contact_email = Column(String(255))
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    users = relationship("OrganizationUser", back_populates="organization")
    programs = relationship("OrganizationProgram", back_populates="organization")


class OrganizationUser(Base):
    __tablename__ = "organization_users"

    organization_id = Column(BigInteger, ForeignKey("organizations.organization_id"), primary_key=True)
    user_id = Column(BigInteger, ForeignKey("users.user_id"), primary_key=True)
    org_role = Column(String(100))
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    organization = relationship("Organization", back_populates="users")
    user = relationship("User", back_populates="organizations")


class OrganizationProgram(Base):
    __tablename__ = "organization_programs"

    organization_id = Column(BigInteger, ForeignKey("organizations.organization_id"), primary_key=True)
    program_id = Column(BigInteger, ForeignKey("programs.program_id"), primary_key=True)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    organization = relationship("Organization", back_populates="programs")
    program = relationship("Program", back_populates="organizations")
