# Assignment_10/creational_patterns/abstract_factory.py
from abc import ABC, abstractmethod

# Abstract Products
class Book(ABC):
    @abstractmethod
    def get_info(self):
        pass

class Author(ABC):
    @abstractmethod
    def get_info(self):
        pass

# Concrete Products - Fiction
class FictionBook(Book):
    def __init__(self, title):
        self.title = title
    
    def get_info(self):
        return f"Fiction Book: {self.title}"

class FictionAuthor(Author):
    def __init__(self, name):
        self.name = name
    
    def get_info(self):
        return f"Fiction Author: {self.name}"

# Concrete Products - Nonfiction
class NonfictionBook(Book):
    def __init__(self, title):
        self.title = title
    
    def get_info(self):
        return f"Non-Fiction Book: {self.title}"

class NonfictionAuthor(Author):
    def __init__(self, name):
        self.name = name
    
    def get_info(self):
        return f"Non-Fiction Author: {self.name}"

# Abstract Factory
class BookstoreFactory(ABC):
    @abstractmethod
    def get_book_factory(self):
        pass
    
    @abstractmethod
    def get_author_factory(self):
        pass

# Concrete Factories
class FictionBookstoreFactory(BookstoreFactory):
    def get_book_factory(self):
        return FictionBookFactory()
    
    def get_author_factory(self):
        return FictionAuthorFactory()

class NonfictionBookstoreFactory(BookstoreFactory):
    def get_book_factory(self):
        return NonfictionBookFactory()
    
    def get_author_factory(self):
        return NonfictionAuthorFactory()

# Product Factories
class FictionBookFactory:
    def create_book(self, title):
        return FictionBook(title)

class FictionAuthorFactory:
    def create_author(self, name):
        return FictionAuthor(name)

class NonfictionBookFactory:
    def create_book(self, title):
        return NonfictionBook(title)

class NonfictionAuthorFactory:
    def create_author(self, name):
        return NonfictionAuthor(name)

# Factory function
def BookstoreFactory(genre: str):
    if genre == "fiction":
        return FictionBookstoreFactory()
    elif genre == "nonfiction":
        return NonfictionBookstoreFactory()
    raise ValueError(f"Unknown genre: {genre}")


class BookFactory:
    def create_book(self, title):
        return FictionBook(title)  # Default to fiction or adjust as needed

class AuthorFactory:
    def create_author(self, name):
        return FictionAuthor(name)  # Default to fiction or adjust as needed

# Make sure these are available for import
__all__ = ['BookstoreFactory', 'BookFactory', 'AuthorFactory']



