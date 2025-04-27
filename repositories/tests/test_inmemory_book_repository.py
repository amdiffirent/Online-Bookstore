import unittest
from repositories.inmemory.inmemory_book_repository import InMemoryBookRepository
from Assignment_10.creational_patterns.abstract_factory import Book
class TestInMemoryBookRepository(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryBookRepository()
        self.book = Book(id="1", title="Test Book", author="Test Author", price=100.0)

    def test_save_and_find_by_id(self):
        self.repo.save(self.book)
        found = self.repo.find_by_id("1")
        self.assertIsNotNone(found)
        self.assertEqual(found.title, "Test Book")

    def test_find_all(self):
        self.repo.save(self.book)
        books = self.repo.find_all()
        self.assertEqual(len(books), 1)

    def test_delete(self):
        self.repo.save(self.book)
        self.repo.delete("1")
        found = self.repo.find_by_id("1")
        self.assertIsNone(found)

if __name__ == '__main__':
    unittest.main()
