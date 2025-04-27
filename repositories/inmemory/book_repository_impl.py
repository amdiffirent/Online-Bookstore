from typing import Dict, Optional, List
from models.book import Book
from repositories.book_repository import BookRepository

class InMemoryBookRepository(BookRepository):
    def __init__(self):
        self._storage: Dict[str, Book] = {}
    
    def save(self, book: Book) -> None:
        self._storage[book.id] = book
    
    def find_by_id(self, id: str) -> Optional[Book]:
        return self._storage.get(id)
    
    def find_all(self) -> List[Book]:
        return list(self._storage.values())
    
    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]