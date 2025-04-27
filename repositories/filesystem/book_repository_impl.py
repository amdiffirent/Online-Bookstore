import json
from typing import Optional, List
from pathlib import Path
from models.book import Book
from repositories.book_repository import BookRepository

class FileSystemBookRepository(BookRepository):
    def __init__(self, file_path: str):
        self._file_path = Path(file_path)
        self._storage = {}
        self._load_from_file()
    
    def _load_from_file(self) -> None:
        if self._file_path.exists():
            with open(self._file_path) as f:
                self._storage = json.load(f)
    
    def _save_to_file(self) -> None:
        with open(self._file_path, 'w') as f:
            json.dump(self._storage, f)
    
    def save(self, book: Book) -> None:
        # TODO: Implement this
        pass
    
    def find_by_id(self, id: str) -> Optional[Book]:
        # TODO: Implement this
        pass
    
    def find_all(self) -> List[Book]:
        # TODO: Implement this
        return []
    
    def delete(self, id: str) -> None:
        # TODO: Implement this
        pass