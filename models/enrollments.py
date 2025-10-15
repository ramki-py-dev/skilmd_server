from sqlalchemy import Column, BigInteger, Enum, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

import enum


class EnrollmentStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    WITHDRAWN = "WITHDRAWN"


class Enrollment(Base):
    __tablename__ = "enrollments"

    enrollment_id = Column(BigInteger, primary_key=True, autoincrement=True)
    course_id = Column(BigInteger, ForeignKey("courses.course_id"), nullable=False)
    user_id = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    status = Column(Enum(EnrollmentStatus), default=EnrollmentStatus.ACTIVE, nullable=False)
    enrolled_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    completed_at = Column(TIMESTAMP)

    user = relationship("User", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

    lesson_progress = relationship("LessonProgress", back_populates="enrollment")
    module_progress = relationship("ModuleProgress", back_populates="enrollment")
    course_progress = relationship("CourseProgress", back_populates="enrollment")
    
    review = relationship("CourseReview", back_populates="enrollment", uselist=False)
    certificate = relationship("Certificate", back_populates="enrollment", uselist=False)
    assignment_submissions = relationship("AssignmentSubmission", back_populates="enrollment")
    extension_requests = relationship("AssignmentExtensionRequest", back_populates="enrollment")
    quiz_attempts = relationship("QuizAttempt", back_populates="enrollment")

