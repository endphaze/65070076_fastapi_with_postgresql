from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
# from sqlalchemy.orm import relationship

from database import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(String, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    dob = Column(Date, index=True)
    gender = Column(String, index=True)

