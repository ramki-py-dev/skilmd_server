from sqlalchemy import Column, BigInteger, String, Text, Enum, Integer, TIMESTAMP, DECIMAL, ForeignKey, func
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

import enum


class QuestionType(str, enum.Enum):
    SINGLE_CHOICE = "SINGLE_CHOICE"
    MULTIPLE_CHOICE = "MULTIPLE_CHOICE"
    FREE_TEXT = "FREE_TEXT"


class Quiz(Base):
    __tablename__ = "quizzes"

    quiz_id = Column(BigInteger, primary_key=True, autoincrement=True)
    lesson_id = Column(BigInteger, ForeignKey("lessons.lesson_id"), unique=True, nullable=False)
    title = Column(String(255), nullable=False)
    passing_score = Column(DECIMAL(6, 2), default=0, nullable=False)
    time_limit_seconds = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

    lesson = relationship("Lesson", back_populates="quiz")
    questions = relationship("QuizQuestion", back_populates="quiz")
    attempts = relationship("QuizAttempt", back_populates="quiz")


class QuizQuestion(Base):
    __tablename__ = "quiz_questions"

    question_id = Column(BigInteger, primary_key=True, autoincrement=True)
    quiz_id = Column(BigInteger, ForeignKey("quizzes.quiz_id"), nullable=False)
    question_text = Column(Text, nullable=False)
    question_type = Column(Enum(QuestionType), default=QuestionType.SINGLE_CHOICE, nullable=False)
    position = Column(Integer, default=1, nullable=False)

    quiz = relationship("Quiz", back_populates="questions")
    options = relationship("QuizOption", back_populates="question")
    answers = relationship("QuizAnswer", back_populates="question")


class QuizOption(Base):
    __tablename__ = "quiz_options"

    option_id = Column(BigInteger, primary_key=True, autoincrement=True)
    question_id = Column(BigInteger, ForeignKey("quiz_questions.question_id"), nullable=False)
    option_text = Column(Text, nullable=False)
    is_correct = Column(Integer, default=0, nullable=False)
    position = Column(Integer, default=1, nullable=False)

    question = relationship("QuizQuestion", back_populates="options")


class QuizAttempt(Base):
    __tablename__ = "quiz_attempts"

    attempt_id = Column(BigInteger, primary_key=True, autoincrement=True)
    quiz_id = Column(BigInteger, ForeignKey("quizzes.quiz_id"), nullable=False)
    enrollment_id = Column(BigInteger, ForeignKey("enrollments.enrollment_id"), nullable=False)
    started_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    submitted_at = Column(TIMESTAMP)
    score = Column(DECIMAL(6, 2))
    passed = Column(Integer)

    quiz = relationship("Quiz", back_populates="attempts")
    enrollment = relationship("Enrollment", back_populates="quiz_attempts")
    answers = relationship("QuizAnswer", back_populates="attempt")


class QuizAnswer(Base):
    __tablename__ = "quiz_answers"

    answer_id = Column(BigInteger, primary_key=True, autoincrement=True)
    attempt_id = Column(BigInteger, ForeignKey("quiz_attempts.attempt_id"), nullable=False)
    question_id = Column(BigInteger, ForeignKey("quiz_questions.question_id"), nullable=False)
    selected_option_id = Column(BigInteger, ForeignKey("quiz_options.option_id"))
    free_text_answer = Column(Text)
    is_correct = Column(Integer)

    attempt = relationship("QuizAttempt", back_populates="answers")
    question = relationship("QuizQuestion", back_populates="answers")
    option = relationship("QuizOption")
