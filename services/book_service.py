from typing import List
from models.book import Book
from repositories.book_repository import BookRepository

class BookService:
    def __init__(self, book_repo: BookRepository):
        self.book_repo = book_repo

    def create_book(self, book: Book) -> Book:
        self.book_repo.save(book)
        return book

    def get_all_books(self) -> List[Book]:
        return self.book_repo.find_all()

    def get_book(self, book_id: str) -> Book:
        book = self.book_repo.find_by_id(book_id)
        if not book:
            raise ValueError(f"Book with ID '{book_id}' not found")
        return book

    def update_book(self, book_id: str, updated_book: Book) -> Book:
        if not self.book_repo.find_by_id(book_id):
            raise ValueError(f"Book with ID '{book_id}' not found")
        self.book_repo.save(updated_book)
        return updated_book

    def delete_book(self, book_id: str) -> None:
        self.book_repo.delete(book_id)
