from repositories.inmemory.book_repository_impl import InMemoryBookRepository
from repositories.book_repository import BookRepository

class RepositoryFactory:
    @staticmethod
    def get_book_repository(storage_type: str = "MEMORY") -> BookRepository:
        if storage_type == "MEMORY":
            return InMemoryBookRepository()
        # We'll add other storage types later
        raise ValueError(f"Unsupported storage type: {storage_type}")