from abc import ABC, abstractmethod
from typing import List
from framework.schema import Book, 

class BookExplorer:
    def __init__(self, data_source: DataSource):
        self.data_source = data_source

    def operate(self, specification) -> list:
        return self.data_source.operate(specification)



class DataSource(ABC):
    @abstractmethod
    def operate(self, specification: Specification):
        pass

class SQLAlchemyDataSource(DataSource):
    def __init__(self, session: Session):
        self.session = session
        self.query = self.session.query(Book)

    def operate(self, specification: Specification):
        return specification.is_satisfied_by(self.query)
    
class APIDataSource(DataSource):
    def __init__(self)
        pass

    def operate(self, specification: Specification):
        pass

class Specification(ABC):
    @abstractmethod
    def is_satisfied_by(self) -> bool:
        pass

class AuthorSpecification(Specification):
    def __init__(self, author: str):
        self.author = author

    def is_satisfied_by(self, query: Query) -> bool:
        return query.filter(Book.author == self.author)
    
class TitleSpecification(Specification):
    def __init__(self, title: str):
        self.title = title

    def is_satisfied_by(self, query: Query) -> bool:
        return query.filter(Book.title == self.title)
class GenreSpecification(Specification):
    def __init__(self, genre: str):
        self.genre = genre

    def is_satisfied_by(self, query: Query) -> bool:
        return query.filter(Book.genre == self.genre) 
    
class GetCategoriesSpecification(Specification):
    def __init__(self):
        pass

    def is_satisfied_by(self, query: Query) -> bool:
        return query.distinct(Book.genre).all()
    
class CompositeSpecification(Specification):
    def __init__(self, specifications: List[Specification]):
        self.specifications = specifications

    def is_satisfied_by(self, query: Query) -> bool:
        for specification in self.specifications:
            query = specification.is_satisfied_by(query)
        return query

class APISpecification(Specification):
    pass

class APIAuthorSpecification(APISpecification):
    def __init__(self, author):
        self.author = author

    def is_satisfied_by(self):
        pass

class APITitleSpecification(APISpecification):
    def __init__(self, title):
        self.title = title

    def is_satisfied_by(self):
        pass

class APIGenreSpecification(APISpecification):
    def __init__(self, genre):
        self.genre = genre

    def is_satisfied_by(self):
        pass

def APICompositeSpecification(APISpecification):
    def __init__(self, specifications: List[APISpecification]):
        self.specifications = specifications

    def is_satisfied_by(self):
        pass 

