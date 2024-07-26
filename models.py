from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Numeric
# from sqlalchemy.orm import relationship

from database import Base



class Student(Base):
    __tablename__ = 'students'

    id = Column(String, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    dob = Column(Date, index=True)
    gender = Column(String, index=True)

class Book(Base):
    __tablename__ = 'books'

    id = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    detail = Column(String, index=True)
    category = Column(String, index=True)
    synopsis = Column(String, index=True)
    year = Column(Numeric, index=True)
    is_published = Column(Boolean, index=True)
