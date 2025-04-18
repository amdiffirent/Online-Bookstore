# Assignment_10/tests/test_simple_factory.py

import unittest
'''from creational_patterns.simple_factory import BookFactory
from Assignment_10.creational_patterns.abstract_factory import BookstoreFactory, BookFactory, AuthorFactory
from creational_patterns.abstract_factory import BookstoreFactory, BookFactory, AuthorFactory'''

from Assignment_10.creational_patterns.abstract_factory import BookstoreFactory
from Assignment_10.creational_patterns.simple_factory import BookFactory

class TestSimpleFactory(unittest.TestCase):

    def test_create_fiction_book(self):
        book = BookFactory.create_book("fiction")
        self.assertEqual(book.genre, "Fiction")
        self.assertEqual(book.get_description(), "A thrilling fictional story.")

    def test_create_nonfiction_book(self):
        book = BookFactory.create_book("nonfiction")
        self.assertEqual(book.genre, "Non-Fiction")
        self.assertEqual(book.get_description(), "An educational non-fiction piece.")

    def test_create_unknown_book(self):
        with self.assertRaises(ValueError):
            BookFactory.create_book("romance")  # Not implemented

