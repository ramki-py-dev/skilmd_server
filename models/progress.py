from sqlalchemy import Column, BigInteger, Enum, TIMESTAMP, ForeignKey, DECIMAL, func
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

import enum


class ProgressStatus(str, enum.Enum):
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"


class LessonProgress(Base):
    __tablename__ = "lesson_progress"

    enrollment_id = Column(BigInteger, ForeignKey("enrollments.enrollment_id"), primary_key=True)
    lesson_id = Column(BigInteger, ForeignKey("lessons.lesson_id"), primary_key=True)
    status = Column(Enum(ProgressStatus), default=ProgressStatus.NOT_STARTED, nullable=False)
    started_at = Column(TIMESTAMP)
    completed_at = Column(TIMESTAMP)

    enrollment = relationship("Enrollment", back_populates="lesson_progress")
    lesson = relationship("Lesson", back_populates="progress")


class ModuleProgress(Base):
    __tablename__ = "module_progress"

    enrollment_id = Column(BigInteger, ForeignKey("enrollments.enrollment_id"), primary_key=True)
    module_id = Column(BigInteger, ForeignKey("course_modules.module_id"), primary_key=True)
    status = Column(Enum(ProgressStatus), default=ProgressStatus.NOT_STARTED, nullable=False)
    completed_at = Column(TIMESTAMP)

    enrollment = relationship("Enrollment", back_populates="module_progress")
    module = relationship("CourseModule", back_populates="progress")


class CourseProgress(Base):
    __tablename__ = "course_progress"

    enrollment_id = Column(BigInteger, ForeignKey("enrollments.enrollment_id"), primary_key=True)
    progress_percent = Column(DECIMAL(5, 2), default=0.00, nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)

    enrollment = relationship("Enrollment", back_populates="course_progress")
