from datetime import datetime
from typing import Optional
from sqlalchemy import Column, TIMESTAMP, VARCHAR, Integer, Boolean, Text, ForeignKey, CHAR, BigInteger, SmallInteger
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__: str = "users"

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, index=True)
    description = Column(Text)
    KeywordsOne = Column(Text)
    KeywordsTwo = Column(Text)
    KeywordsThree = Column(Text)
    date_course = Column(TIMESTAMP, nullable=False)
    link = Column(Text, nullable=False)


