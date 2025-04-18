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










'''tests/test_prototype.py
import unittest
from Assignment_10.creational_patterns.prototype import ShapeCache, Circle, Rectangle
from Assignment_10.creational_patterns.abstract_factory import BookstoreFactory, BookFactory, AuthorFactory
#from creational_patterns.abstract_factory import BookstoreFactory, BookFactory, AuthorFactory

class TestPrototypePattern(unittest.TestCase):

    def test_clone_circle(self):
        original = Circle(5)
        clone = original.clone()
        self.assertIsNot(original, clone)
        self.assertEqual(clone.radius, 5)
        self.assertEqual(clone.draw(), "Drawing a circle with radius 5")

    def test_clone_rectangle(self):
        original = Rectangle(10, 5)
        clone = original.clone()
        self.assertIsNot(original, clone)
        self.assertEqual(clone.width, 10)
        self.assertEqual(clone.height, 5)
        self.assertEqual(clone.draw(), "Drawing a rectangle 10x5")

    def test_shape_cache_clone(self):
        ShapeCache.load_cache()
        cloned_circle = ShapeCache.get_shape("circle")
        self.assertIsInstance(cloned_circle, Circle)
        self.assertEqual(cloned_circle.draw(), "Drawing a circle with radius 5")

if __name__ == '__main__':
    unittest.main() '''
