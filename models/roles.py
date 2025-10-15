from sqlalchemy import Column, String, BigInteger, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Role(Base):
    __tablename__ = "roles"

    role_id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    users = relationship("UserRole", back_populates="role")

class UserRole(Base):
    __tablename__ = "user_roles"

    user_id = Column(BigInteger, ForeignKey("users.user_id", ondelete="CASCADE"), primary_key=True)
    role_id = Column(BigInteger, ForeignKey("roles.role_id", ondelete="RESTRICT"), primary_key=True)
    assigned_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    user = relationship("User", back_populates="roles")
    role = relationship("Role", back_populates="users")
