from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class BookCreate(BaseModel):
    """
    Represents a book creation request.
    """
    title: str
    author: str
    genre: str
    seller_id: int
    isbn: str
    price: float
    created_at: datetime
    modified_at: datetime
    delete_flag: bool = False

class Categories(Enum):
    HORROR = 'horror'
    THRILLER = 'thriller'
    ROMANCE = 'romance'
    FANTASY = 'fantasy'
    SCIFI = 'scifi'
    BIOGRAPHY = 'biography'
    HISTORY = 'history'
    MYSTERY = 'mystery'
    COMICS = 'comics'
    SCIENCE = 'science'
    FICTION = 'fiction'
    NONFICTION = 'nonfiction'
    CHILDREN = 'children'
    CLASSICS = 'classics'