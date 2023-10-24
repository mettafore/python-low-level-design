"""
Book Service API Paths:

POST /books - Upload a new book (For Sellers/Admin)
GET /books - Get the list of all available books
GET /books/{book_id} - Get details of a specific book
PUT /books/{book_id} - Update details of a specific book (For Sellers/Admin)
DELETE /books/{book_id} - Delete a specific book (For Sellers/Admin)
"""

from services.BooksService import BooksService
from fastapi import Depends, HTTPException, APIRouter, status, Header
from services.AuthService import PasswordAuthStrategy

book_router = APIRouter(prefix="/books", tags=["Book"])


@book_router.post("/")
async def upload_book(session: Session = Depends(get_session)):
    pass


@book_router.get("/")
async def get_all_books(session: Session = Depends(get_session)):
    pass

@book_router.get("/page/{page_number}")
async def get_all_books_page(page_number: int, session: Session = Depends(get_session)):
    return BooksService(session).get_all_books_page(page_number)


@book_router.get("/{book_id}")
async def get_book(book_id: int, session: Session = Depends(get_session)):
    pass


@book_router.put("/{book_id}")
async def update_book(book_id: int, book_data: BookCreate, session: Session = Depends(get_session)):
    return BooksService(session).update_book(book_id, book_data, session)


@book_router.delete("/{book_id}")
async def delete_book(book_id: int, session: Session = Depends(get_session), payload=Depends(PasswordAuthStrategy().decode_token)):
    print(payload)
    # return BookService(session).delete_book(book_id)
