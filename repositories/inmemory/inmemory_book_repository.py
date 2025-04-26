from repositories.book_repository import BookRepository
from Assignment_10.creational_patterns.abstract_factory import Book
from typing import Optional, List

class InMemoryBookRepository(BookRepository):
    def __init__(self):
        self._storage = {}  # This acts like our database (a simple dictionary)

    def save(self, entity: Book) -> None:
        self._storage[entity.id] = entity

    def find_by_id(self, id: str) -> Optional[Book]:
        return self._storage.get(id)

    def find_all(self) -> List[Book]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
