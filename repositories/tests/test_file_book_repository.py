import unittest
import tempfile
import os
from ..file.file_book_repository import FileBookRepository
from ..simple_book import Book

class TestFileBookRepository(unittest.TestCase):
    def setUp(self):
        # Create a properly initialized temp file
        self.temp_file = tempfile.NamedTemporaryFile(suffix='.json', delete=False)
        # Explicitly write valid empty JSON array
        self.temp_file.write(b'[]')  # Note the 'b' for bytes in Python 3
        self.temp_file.close()
        self.repo = FileBookRepository(self.temp_file.name)
        self.test_book = Book("1", "Test Book", "Test Author", "2023")

    def tearDown(self):
        try:
            os.unlink(self.temp_file.name)
        except:
            pass

    def test_handles_empty_file(self):
        """Test repository works with empty JSON file"""
        # Verify empty file
        with open(self.temp_file.name, 'r') as f:
            self.assertEqual(f.read().strip(), '[]')
        
        # Test operations
        self.assertEqual(len(self.repo.find_all()), 0)
        self.repo.save(self.test_book)
        self.assertEqual(len(self.repo.find_all()), 1)

    # Rest of your test methods...
    def test_save_and_find(self):
        self.repo.save(self.test_book)
        found = self.repo.find_by_id("1")
        self.assertEqual(found.title, "Test Book")

    def test_delete(self):
        self.repo.save(self.test_book)
        self.repo.delete("1")
        self.assertIsNone(self.repo.find_by_id("1"))

if __name__ == '__main__':
    unittest.main()