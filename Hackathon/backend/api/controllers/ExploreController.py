"""
Book Search and Browse API Paths:

GET /books/search - Search books with various criteria (For Buyers)
GET /books/category/{category_name} - Browse books by category (For Buyers)
"""

from fastapi import Depends, HTTPException, APIRouter, status, Header
from services.ExploreService import BooksExplorer
from framework.database import get_session

explore_router = APIRouter(prefix="/books", tags=["Explore"])


@explore_router.get("/search")
def search_books(author: str = None, title: str = None, session: Session = Depends(get_session)):
    strategy = OperationStrategy(SQLAlchemyDataSource(), db)
    if author:
        return strategy.operate(AuthorSpecification(author))
    elif title:
        return strategy.operate(TitleSpecification(title))
    return []

@explore_router.get("/category/{category_name}")
def browse_books(genre: str, session: Session = Depends(get_session)):
    strategy = BrowseStrategy(SQLAlchemyDataSource(), db)
    return strategy.operate(GenreSpecification(category_name))
