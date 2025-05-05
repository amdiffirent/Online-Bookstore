
import pytest
from online_bookstore.services.book_service import BookService
from online_bookstore.models.book import Book

class MockBookRepository:
    def __init__(self):
        self.books = {}

    def save(self, book):
        self.books[book.id] = book
        return book

    def find_all(self):
        return list(self.books.values())

    def find_by_id(self, book_id):
        return self.books.get(book_id)

    def delete(self, book_id):
        if book_id in self.books:
            del self.books[book_id]

@pytest.fixture
def book_repo():
    return MockBookRepository()

@pytest.fixture
def book_service(book_repo):
    return BookService(book_repo)

def test_create_book(book_service):
    book = Book(id="1", title="Test Book", author="Author A", price=99.99)
    created = book_service.create_book(book)
    assert created.title == "Test Book"

def test_get_all_books(book_service):
    book1 = Book(id="1", title="Book 1", author="A", price=10.0)
    book2 = Book(id="2", title="Book 2", author="B", price=15.0)
    book_service.create_book(book1)
    book_service.create_book(book2)
    books = book_service.get_all_books()
    assert len(books) == 2

def test_get_book_valid(book_service):
    book = Book(id="1", title="Book 1", author="A", price=10.0)
    book_service.create_book(book)
    found = book_service.get_book("1")
    assert found.id == "1"

def test_get_book_invalid(book_service):
    with pytest.raises(ValueError):
        book_service.get_book("non-existent")
