from repositories.repository import Repository
from Assignment_10.creational_patterns.abstract_factory import Book
from typing import Optional, List

class BookRepository(Repository[Book, str]):
    def save(self, entity: Book) -> None:
        """Create or Update a Book"""
        raise NotImplementedError

    def find_by_id(self, id: str) -> Optional[Book]:
        """Find a Book by ID"""
        raise NotImplementedError

    def find_all(self) -> List[Book]:
        """Find all Books"""
        raise NotImplementedError

    def delete(self, id: str) -> None:
        """Delete a Book by ID"""
        raise NotImplementedError
