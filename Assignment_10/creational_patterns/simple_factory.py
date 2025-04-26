# Assignment_10/creational_patterns/simple_factory.py
from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, genre):
        self.genre = genre
    
    @abstractmethod
    def get_description(self):
        pass

class FictionBook(Book):
    def get_description(self):
        return "A thrilling fictional story."

class NonfictionBook(Book):
    def get_description(self):
        return "An educational non-fiction piece."

class BookFactory:
    @staticmethod
    def create_book(genre):
        if genre == "fiction":
            return FictionBook("Fiction")
        elif genre == "nonfiction":
            return NonfictionBook("Non-Fiction")
        raise ValueError(f"Unknown genre: {genre}")


