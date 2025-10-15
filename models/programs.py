from sqlalchemy import Column, String, BigInteger, Text, Date, TIMESTAMP, ForeignKey, func, Enum
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

import enum


class EnrollmentStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    WITHDRAWN = "WITHDRAWN"


class Program(Base):
    __tablename__ = "programs"

    program_id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    slug = Column(String(120), unique=True, nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    created_by = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    organizations = relationship("OrganizationProgram", back_populates="program")
    enrollments = relationship("ProgramEnrollment", back_populates="program")
    courses = relationship("ProgramCourse", back_populates="program")
    users = relationship("User", back_populates="programs")


class ProgramEnrollment(Base):
    __tablename__ = "program_enrollments"

    program_enrollment_id = Column(BigInteger, primary_key=True, autoincrement=True)
    program_id = Column(BigInteger, ForeignKey("programs.program_id"), nullable=False)
    user_id = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    status = Column(Enum(EnrollmentStatus), default=EnrollmentStatus.ACTIVE, nullable=False)
    enrolled_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    program = relationship("Program", back_populates="enrollments")
    user = relationship("User", back_populates="program_enrollments")


class ProgramCourse(Base):
    __tablename__ = "program_courses"

    program_id = Column(BigInteger, ForeignKey("programs.program_id"), primary_key=True)
    course_id = Column(BigInteger, ForeignKey("courses.course_id"), primary_key=True)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    program = relationship("Program", back_populates="courses")
    course = relationship("Course", back_populates="programs")
