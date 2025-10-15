from sqlalchemy import Column, BigInteger, String, Text, DECIMAL, TIMESTAMP, ForeignKey, Enum, func
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

import enum


class Assignment(Base):
    __tablename__ = "assignments"

    assignment_id = Column(BigInteger, primary_key=True, autoincrement=True)
    lesson_id = Column(BigInteger, ForeignKey("lessons.lesson_id"), unique=True, nullable=False)
    title = Column(String(255), nullable=False)
    instructions = Column(Text)
    due_at = Column(TIMESTAMP)
    max_points = Column(DECIMAL(6, 2), default=100, nullable=False)

    lesson = relationship("Lesson", back_populates="assignment")
    submissions = relationship("AssignmentSubmission", back_populates="assignment")
    extension_requests = relationship("AssignmentExtensionRequest", back_populates="assignment")


class AssignmentSubmission(Base):
    __tablename__ = "assignment_submissions"

    submission_id = Column(BigInteger, primary_key=True, autoincrement=True)
    assignment_id = Column(BigInteger, ForeignKey("assignments.assignment_id"), nullable=False)
    enrollment_id = Column(BigInteger, ForeignKey("enrollments.enrollment_id"), nullable=False)
    submitted_at = Column(TIMESTAMP)
    file_url = Column(String(500))
    grade = Column(DECIMAL(6, 2))
    feedback = Column(Text)

    assignment = relationship("Assignment", back_populates="submissions")
    enrollment = relationship("Enrollment", back_populates="assignment_submissions")


class ExtensionStatus(str, enum.Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    DENIED = "DENIED"


class AssignmentExtensionRequest(Base):
    __tablename__ = "assignment_extension_requests"

    request_id = Column(BigInteger, primary_key=True, autoincrement=True)
    assignment_id = Column(BigInteger, ForeignKey("assignments.assignment_id"), nullable=False)
    enrollment_id = Column(BigInteger, ForeignKey("enrollments.enrollment_id"), nullable=False)
    requested_until = Column(TIMESTAMP, nullable=False)
    reason = Column(Text)
    status = Column(Enum(ExtensionStatus), default=ExtensionStatus.PENDING, nullable=False)
    reviewed_by = Column(BigInteger, ForeignKey("users.user_id"))
    reviewed_at = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

    assignment = relationship("Assignment", back_populates="extension_requests")
    enrollment = relationship("Enrollment", back_populates="extension_requests")
    reviewer = relationship("User")
