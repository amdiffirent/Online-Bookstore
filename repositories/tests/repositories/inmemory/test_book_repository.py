import pytest
from models.book import Book
from repositories.inmemory.book_repository_impl import InMemoryBookRepository

def test_save_and_find_book():
    repo = InMemoryBookRepository()
    book = Book(id="1", title="Test Book", author="Test Author")
    
    # Test save
    repo.save(book)
    
    # Test find_by_id
    found = repo.find_by_id("1")
    assert found is not None
    assert found.title == "Test Book"
    
    # Test find_all
    all_books = repo.find_all()
    assert len(all_books) == 1
    
    # Test delete
    repo.delete("1")
    assert repo.find_by_id("1") is None