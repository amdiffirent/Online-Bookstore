from abc import ABC
from models.book import Book  # Assuming you have a Book model
from repositories.repository import Repository

class BookRepository(Repository[Book, str], ABC):
    """Book-specific repository interface"""
    pass