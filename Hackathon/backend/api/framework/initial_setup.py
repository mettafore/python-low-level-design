from framework.schema import User, Book
from models.user_model import Role
from framework.database import Session
from fastapi import Depends
from sqlalchemy import exc
from bcrypt import hashpw, gensalt

def initial_setup():
    session = Session()
    try:
        # Create a User Seller
        seller = User(email='seller@example.com', password=hashpw('password'.encode(), gensalt()), role=Role.SELLER)
        session.add(seller)
        session.commit()

        # Add real books with real genres
        book1 = Book(title='To Kill a Mockingbird', author='Harper Lee', genre='Fiction', seller_id=seller.id, isbn='1234567890', price=10.0)
        book2 = Book(title='1984', author='George Orwell', genre='Fiction', seller_id=seller.id, isbn='0987654321', price=20.0)
        book3 = Book(title='The Great Gatsby', author='F. Scott Fitzgerald', genre='Fiction', seller_id=seller.id, isbn='2345678901', price=15.0)
        book4 = Book(title='A Brief History of Time', author='Stephen Hawking', genre='Science', seller_id=seller.id, isbn='3456789012', price=25.0)
        book5 = Book(title='The Selfish Gene', author='Richard Dawkins', genre='Science', seller_id=seller.id, isbn='4567890123', price=30.0)
        book6 = Book(title='The Origin of Species', author='Charles Darwin', genre='Science', seller_id=seller.id, isbn='5678901234', price=35.0)
        book7 = Book(title='The Art of War', author='Sun Tzu', genre='History', seller_id=seller.id, isbn='6789012345', price=40.0)
        book8 = Book(title='The Diary of a Young Girl', author='Anne Frank', genre='History', seller_id=seller.id, isbn='7890123456', price=45.0)
        book9 = Book(title='Guns, Germs, and Steel', author='Jared Diamond', genre='History', seller_id=seller.id, isbn='8901234567', price=50.0)
        session.add_all([book1, book2, book3, book4, book5, book6, book7, book8, book9])
        session.commit()
