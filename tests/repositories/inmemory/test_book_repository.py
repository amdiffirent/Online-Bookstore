import pytest
from models.book import Book
from repositories.inmemory.book_repository_impl import InMemoryBookRepository

@pytest.fixture
def repo():
    return InMemoryBookRepository()

@pytest.fixture
def sample_book():
    return Book(id="1", title="Test Book", author="Test Author")

def test_save_and_retrieve_book(repo, sample_book):
    repo.save(sample_book)
    assert repo.find_by_id("1") == sample_book

def test_find_nonexistent_book(repo):
    assert repo.find_by_id("999") is None

def test_save_duplicate_id(repo, sample_book):
    repo.save(sample_book)
    with pytest.raises(ValueError):
        duplicate = Book(id="1", title="Duplicate", author="Author")
        repo.save(duplicate)

def test_delete_book(repo, sample_book):
    repo.save(sample_book)
    repo.delete("1")
    assert repo.find_by_id("1") is None

def test_find_all_books(repo, sample_book):
    repo.save(sample_book)
    repo.save(Book(id="2", title="Book 2", author="Author 2"))
    assert len(repo.find_all()) == 2

def test_find_by_title(repo):
    repo.save(Book(id="1", title="Python Programming", author="A"))
    repo.save(Book(id="2", title="Java Programming", author="B"))
    results = repo.find_by_title("python")
    assert len(results) == 1
    assert results[0].title == "Python Programming"

def test_count_books(repo):
    assert repo.count() == 0
    repo.save(Book(id="1", title="Book 1", author="A"))
    assert repo.count() == 1