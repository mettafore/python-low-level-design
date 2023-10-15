class  BooksService:
    def __init__(self):
        pass

    def upload_book(self):
        pass

    def get_book(self):
        pass

    def get_all_books(self):
        pass

    def update_book(self):
        pass

    def delete_book(self):
        pass


class BookDirector:
    def __init__(self, builder: BookBuilder):
        self.builder = builder

    def construct(self, book_data: BookCreate):
        self.builder.set_title(book_data.title)
        self.builder.set_author(book_data.author)
        self.builder.set_genre(book_data.genre)
        self.builder.set_isbn(book_data.isbn)
        self.builder.set_price(book_data.price)
        self.builder.set_seller_id(book_data.seller_id)
        self.builder.set_delete_flag(book_data.delete_flag)
        self.builder.set_seller(book_data.seller)
        self.builder.set_orders(book_data.orders)
        return self.builder.get_result()
    
class BookBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self.book = Book("", "", 0.0)

    def set_title(self, title: str) -> 'BookBuilder':
        self.book.title = title
        return self

    def set_author(self, author: str) -> 'BookBuilder':
        self.book.author = author
        return self

    def set_price(self, price: float) -> 'BookBuilder':
        self.book.price = price
        return self

    def set_description(self, description: str) -> 'BookBuilder':
        self.book.description = description
        return self

    def build(self) -> Book:
        book = self.book
        self.reset()
        return book