from sqlalchemy import Column, String, BigInteger, Text, Boolean, Enum, TIMESTAMP, func, ForeignKey, Integer
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

import enum

class CourseLevel(str, enum.Enum):
    BEGINNER = "BEGINNER"
    INTERMEDIATE = "INTERMEDIATE"
    ADVANCED = "ADVANCED"

class Course(Base):
    __tablename__ = "courses"

    course_id = Column(BigInteger, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    course_code = Column(String(64), unique=True)
    description = Column(Text)
    level = Column(Enum(CourseLevel), default=CourseLevel.BEGINNER, nullable=False)
    language = Column(String(20), default="en", nullable=False)
    is_published = Column(Boolean, default=False, nullable=False)
    created_by = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    modules = relationship("CourseModule", back_populates="course")
    enrollments = relationship("Enrollment", back_populates="course")
    reviews = relationship("CourseReview", back_populates="course")
    programs = relationship("ProgramCourse", back_populates="course")
    invitations = relationship("CourseInvitation", back_populates="course")
    instructors = relationship("CourseInstructor", back_populates="course")

class CourseInstructor(Base):
    __tablename__ = "course_instructors"

    course_id = Column(BigInteger, ForeignKey("courses.course_id"), primary_key=True)
    user_id = Column(BigInteger, ForeignKey("users.user_id"), primary_key=True)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    course = relationship("Course", back_populates="instructors")
    user = relationship("User", back_populates="instructed_courses")

class CourseModule(Base):
    __tablename__ = "course_modules"

    module_id = Column(BigInteger, primary_key=True, autoincrement=True)
    course_id = Column(BigInteger, ForeignKey("courses.course_id"), unique=True, nullable=False)
    title = Column(String(255), nullable=False)
    position = Column(Integer, default=1, unique=True, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    course = relationship("Course", back_populates="modules")
    lessons = relationship("Lesson", back_populates="module")
