import unittest
# from creational_patterns.abstract_factory import BookstoreFactory, BookFactory, AuthorFactory

from Assignment_10.creational_patterns.abstract_factory import BookstoreFactory, BookFactory, AuthorFactory

class TestAbstractFactory(unittest.TestCase):

    def test_create_fiction_book_and_author(self):
        factory = BookstoreFactory("fiction")
        book_factory = factory.get_book_factory()
        author_factory = factory.get_author_factory()

        book = book_factory.create_book("The Fictional Life")
        author = author_factory.create_author("John Novel")

        self.assertEqual(book.get_info(), "Fiction Book: The Fictional Life")
        self.assertEqual(author.get_info(), "Fiction Author: John Novel")

    def test_create_nonfiction_book_and_author(self):
        factory = BookstoreFactory("nonfiction")
        book_factory = factory.get_book_factory()
        author_factory = factory.get_author_factory()

        book = book_factory.create_book("Real Stories")
        author = author_factory.create_author("Jane Facts")

        self.assertEqual(book.get_info(), "Non-Fiction Book: Real Stories")
        self.assertEqual(author.get_info(), "Non-Fiction Author: Jane Facts")

    def test_invalid_genre_raises_error(self):
        with self.assertRaises(ValueError):
            BookstoreFactory("mystery")

if __name__ == '__main__':
    unittest.main()
