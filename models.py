from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.orm import relationship

from database import Base



class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    dob = Column(Date, index=True)
    gender = Column(String, index=True)

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    detail = Column(String, index=True)
    category = Column(String, index=True)
    synopsis = Column(String, index=True)
    year = Column(String, index=True)
    is_published = Column(Boolean, index=True)

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    note =  Column(String, index=True, autoincrement=True)
    
    

class Coffee(Base):
    __tablename__ = 'coffees'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Numeric, index=True)


class OrderDetail(Base):
    __tablename__ = 'orderDetails'
    
    order_id = Column(Integer, ForeignKey('orders.id'), primary_key=True, index=True)
    coffee_id = Column(Integer, ForeignKey('coffees.id'), primary_key=True, index=True)
    
    
    quantity = Column(Integer, nullable=False, default=1)



