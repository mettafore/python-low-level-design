from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, Enum, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from models.user_model import Role
from models.transaction_model import TransactionStatus
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum(Role), nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    modified_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    books = relationship('Book', back_populates='seller')
    orders = relationship('Order', back_populates='buyer')  # Add this line



class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String)
    seller_id = Column(Integer, ForeignKey('users.id'))
    isbn = Column(String, unique=True)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    modified_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    delete_flag = Column(Boolean, default=False)

    seller = relationship('User', back_populates='books')
    orders = relationship('Order', back_populates='book')


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    buyer_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Float, nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'))
    created_at = Column(DateTime, default=datetime.utcnow)

    buyer = relationship('User', back_populates='orders')
    book = relationship('Book', back_populates='orders')


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    amount = Column(Float, nullable=False)
    status = Column(Enum(TransactionStatus), nullable=False)  # Can be more specific with Enum if you have predefined statuses
    payment_type_id = Column(Integer, ForeignKey('paymenttypes.id'))


class PaymentType(Base):
    __tablename__ = 'paymenttypes'

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)