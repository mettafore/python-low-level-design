"""
Book Search and Browse API Paths:

GET /books/search - Search books with various criteria (For Buyers)
GET /books/category/{category_name} - Browse books by category (For Buyers)
"""

from fastapi import Depends, HTTPException, APIRouter, status, Header
from services.ExploreService import BooksExplorer
from framework.database import get_session
from services.ExploreService import (
    BookExplorer, 
    SQLAlchemyDataSource, 
    GetCategoriesSpecification, 
    AuthorSpecification, 
    TitleSpecification, 
    GenreSpecification
)

explore_router = APIRouter(prefix="/books", tags=["Explore"])


@explore_router.get("/search")
def search_books(author: str = None, title: str = None, session: Session = Depends(get_session)):
    specifications = []
    if author:
        specifications.append(AuthorSpecification(author))
    if title:
        specifications.append(TitleSpecification(title))

    if len(specifications) > 1:
        specification = CompositeSpecification(specifications)
    else:
        specification = specifications[0]
    return BookExplorer(SQLAlchemyDataSource(session)).operate(specification)


@explore_router.get("/category/{category_name}")
def browse_books(session: Session = Depends(get_session)):
    specification = GenreSpecification(category_name)
    return BookExplorer(SQLAlchemyDataSource(session)).operate(specification)

@explore_router.get("/categories")
def get_categories(session: Session = Depends(get_session)):
    return BookExplorer(SQLAlchemyDataSource(session)).operate(GetCategoriesSpecification())
