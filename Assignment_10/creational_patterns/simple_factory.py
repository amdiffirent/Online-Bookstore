# Book class (base class)
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, Price: {self.price}"

# Concrete book types
class Paperback(Book):
    def __str__(self):
        return f"Paperback: {self.title} by {self.author}, Price: {self.price}"

class Ebook(Book):
    def __str__(self):
        return f"Ebook: {self.title} by {self.author}, Price: {self.price}"

class Audiobook(Book):
    def __str__(self):
        return f"Audiobook: {self.title} by {self.author}, Price: {self.price}"

# Simple Factory
class BookFactory:
    @staticmethod
    def create_book(book_type, title, author, price):
        if book_type == "paperback":
            return Paperback(title, author, price)
        elif book_type == "ebook":
            return Ebook(title, author, price)
        elif book_type == "audiobook":
            return Audiobook(title, author, price)
        else:
            raise ValueError(f"Unknown book type: {book_type}")

# Example usage of the factory
book1 = BookFactory.create_book("paperback", "The Great Gatsby", "F. Scott Fitzgerald", 19.99)
book2 = BookFactory.create_book("ebook", "1984", "George Orwell", 9.99)

print(book1)
print(book2)
