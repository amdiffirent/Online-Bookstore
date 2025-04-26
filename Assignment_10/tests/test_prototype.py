# Assignment_10/tests/test_prototype.py
import unittest
from Assignment_10.creational_patterns.prototype import Book, BookCache

class TestPrototypePattern(unittest.TestCase):
    def test_clone_book(self):
        original = Book("The Great Gatsby", "F. Scott Fitzgerald", 12.99, "Classic")
        clone = original.clone()
        
        self.assertIsNot(original, clone)
        self.assertEqual(clone.title, "The Great Gatsby")
        self.assertEqual(str(clone), "The Great Gatsby by F. Scott Fitzgerald ($12.99, Classic)")

    def test_book_cache(self):
        BookCache.load_cache()
        
        # Get a cloned bestseller
        bestseller = BookCache.get_book('bestseller')
        self.assertEqual(bestseller.price, 14.99)
        
        # Modify the clone without affecting the prototype
        bestseller.title = "Specific Bestseller"
        bestseller.price = 9.99
        
        # Get another copy from cache
        another_copy = BookCache.get_book('bestseller')
        self.assertEqual(another_copy.price, 14.99)  # Original price unchanged

if __name__ == '__main__':
    unittest.main()


