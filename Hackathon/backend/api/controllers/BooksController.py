"""
Book Service API Paths:

POST /books - Upload a new book (For Sellers/Admin)
GET /books - Get the list of all available books
GET /books/{book_id} - Get details of a specific book
PUT /books/{book_id} - Update details of a specific book (For Sellers/Admin)
DELETE /books/{book_id} - Delete a specific book (For Sellers/Admin)
"""

from fastapi import Depends, HTTPException, APIRouter, status, Header

book_router = APIRouter(prefix="/books", tags=["Book"])


@book_router.post("/")
async def upload_book():
    pass


@book_router.get("/")
async def get_all_books():
    pass


@book_router.get("/{book_id}")
async def get_book(book_id: int):
    pass


@book_router.put("/{book_id}")
async def update_book(book_id: int):
    pass


@book_router.delete("/{book_id}")
async def delete_book(book_id: int):
    pass
