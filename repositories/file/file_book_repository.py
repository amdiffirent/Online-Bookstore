import json
import os
from pathlib import Path
from typing import List, Optional
from ..simple_book import Book

class FileBookRepository:
    def __init__(self, filename: str = "books.json"):
        self.filename = filename
        self._ensure_valid_file()

    def _ensure_valid_file(self):
        """Guarantees the file exists with valid JSON array"""
        try:
            # Create parent directories if needed
            Path(self.filename).parent.mkdir(parents=True, exist_ok=True)
            
            # Initialize with empty array if file doesn't exist or is empty/invalid
            if not os.path.exists(self.filename) or os.path.getsize(self.filename) == 0:
                with open(self.filename, 'w') as f:
                    json.dump([], f)
            else:
                # Verify file contains valid JSON
                with open(self.filename, 'r') as f:
                    json.load(f)  # Test parse
        except (json.JSONDecodeError, OSError):
            # Overwrite corrupt file
            with open(self.filename, 'w') as f:
                json.dump([], f)

    def _load_books(self) -> List[Book]:
        """Bulletproof JSON loading"""
        try:
            with open(self.filename, 'r') as f:
                content = f.read().strip()
                if not content:  # Handle truly empty files
                    return []
                return [Book.from_dict(item) for item in json.loads(content)]
        except (json.JSONDecodeError, FileNotFoundError):
            return []  # Fail gracefully

    def _save_books(self, books: List[Book]):
        """Atomic write operation"""
        temp_file = f"{self.filename}.tmp"
        with open(temp_file, 'w') as f:
            json.dump([book.to_dict() for book in books], f, indent=4)
        os.replace(temp_file, self.filename)  # Atomic operation

    # Rest of your methods remain unchanged...
    def save(self, book: Book) -> None:
        books = self._load_books()
        books = [b for b in books if b.id != book.id]
        books.append(book)
        self._save_books(books)

    def find_by_id(self, id: str) -> Optional[Book]:
        books = self._load_books()
        return next((b for b in books if b.id == id), None)

    def find_all(self) -> List[Book]:
        return self._load_books()

    def delete(self, id: str) -> None:
        books = self._load_books()
        books = [b for b in books if b.id != id]
        self._save_books(books)