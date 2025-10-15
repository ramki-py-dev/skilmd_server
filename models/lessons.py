from sqlalchemy import Column, String, BigInteger, Text, Enum, Integer, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

import enum

class LessonType(str, enum.Enum):
    VIDEO = "VIDEO"
    ARTICLE = "ARTICLE"
    QUIZ = "QUIZ"
    ASSIGNMENT = "ASSIGNMENT"
    LAB = "LAB"

class Lesson(Base):
    __tablename__ = "lessons"

    lesson_id = Column(BigInteger, primary_key=True, autoincrement=True)
    module_id = Column(BigInteger, ForeignKey("course_modules.module_id"), nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(Text)
    lesson_type = Column(Enum(LessonType), default=LessonType.VIDEO, nullable=False)
    video_url = Column(String(500))
    duration_seconds = Column(Integer)
    position = Column(Integer, default=1, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    module = relationship("CourseModule", back_populates="lessons")
