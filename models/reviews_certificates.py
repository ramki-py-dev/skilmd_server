from sqlalchemy import Column, BigInteger, String, Text, TIMESTAMP, DECIMAL, ForeignKey, CheckConstraint, func
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class CourseReview(Base):
    __tablename__ = "course_reviews"

    review_id = Column(BigInteger, primary_key=True, autoincrement=True)
    enrollment_id = Column(BigInteger, ForeignKey("enrollments.enrollment_id"), unique=True, nullable=False)
    user_id = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    course_id = Column(BigInteger, ForeignKey("courses.course_id"), nullable=False)
    rating = Column(BigInteger, nullable=False)
    review_text = Column(Text)
    reviewed_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

    __table_args__ = (
        CheckConstraint("rating BETWEEN 1 AND 5", name="chk_rating"),
    )

    enrollment = relationship("Enrollment", back_populates="review")
    user = relationship("User", back_populates="reviews")
    course = relationship("Course", back_populates="reviews")


class Certificate(Base):
    __tablename__ = "certificates"

    certificate_id = Column(BigInteger, primary_key=True, autoincrement=True)
    enrollment_id = Column(BigInteger, ForeignKey("enrollments.enrollment_id"), unique=True, nullable=False)
    serial_number = Column(String(64), unique=True, nullable=False)
    issued_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    file_url = Column(String(500))

    enrollment = relationship("Enrollment", back_populates="certificate")
