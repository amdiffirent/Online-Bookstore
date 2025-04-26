# Assignment_10/creational_patterns/prototype.py
import copy
from abc import ABC, abstractmethod

class BookPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class Book(BookPrototype):
    def __init__(self, title, author, price, genre):
        self.title = title
        self.author = author
        self.price = price
        self.genre = genre
    
    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"{self.title} by {self.author} (${self.price}, {self.genre})"

class BookCache:
    _books = {}
    
    @classmethod
    def load_cache(cls):
        # Pre-load some common book templates
        cls._books['bestseller'] = Book(
            "Generic Bestseller", 
            "Popular Author", 
            14.99, 
            "Fiction"
        )
        cls._books['textbook'] = Book(
            "Academic Textbook", 
            "Professor Expert", 
            89.99, 
            "Non-Fiction"
        )
    
    @classmethod
    def get_book(cls, book_type):
        """Get a cloned book of the specified type"""
        return cls._books.get(book_type).clone()
    
    @classmethod
    def add_book_template(cls, book_type, book):
        """Add a new book template to the cache"""
        cls._books[book_type] = book

