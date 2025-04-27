import pytest
import os
import tempfile
from models.book import Book
from repositories.filesystem.book_repository_impl import FileSystemBookRepository

@pytest.fixture
def temp_repo():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.close()
        repo = FileSystemBookRepository(tmp.name)
        yield repo
        os.unlink(tmp.name)

def test_json_save_and_load(temp_repo):
    book = Book(id="1", title="JSON Book", author="Test")
    temp_repo.save(book)
    
    # Verify data persists
    new_repo = FileSystemBookRepository(temp_repo._file_path)
    assert new_repo.find_by_id("1").title == "JSON Book"