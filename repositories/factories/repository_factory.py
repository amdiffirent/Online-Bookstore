from typing import Optional
from repositories.inmemory.book_repository_impl import InMemoryBookRepository
from repositories.filesystem.book_repository_impl import FileSystemBookRepository
from repositories.book_repository import BookRepository

class RepositoryFactory:
    """
    Factory for creating repository instances with different storage backends.
    
    Supported storage types:
    - "MEMORY": In-memory storage (default)
    - "JSON": File system storage with JSON serialization
    """
    
    @staticmethod
    def get_book_repository(storage_type: str = "MEMORY") -> BookRepository:
        """
        Creates a BookRepository instance for the specified storage type.
        
        Args:
            storage_type: The storage backend to use ("MEMORY" or "JSON")
            
        Returns:
            An instance of BookRepository implementation
            
        Raises:
            ValueError: If an unsupported storage type is provided
        """
        storage_type = storage_type.upper().strip()
        
        if storage_type == "MEMORY":
            return InMemoryBookRepository()
            
        if storage_type == "JSON":
            # Default file path, can be made configurable
            return FileSystemBookRepository("data/books.json")
            
        supported_types = ["MEMORY", "JSON"]
        raise ValueError(
            f"Unsupported storage type: {storage_type}. "
            f"Supported types are: {', '.join(supported_types)}"
        )