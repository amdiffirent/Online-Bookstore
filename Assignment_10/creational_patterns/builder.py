# Book class
class Book:
    def __init__(self):
        self.title = None
        self.author = None
        self.price = None
        self.genre = None
        self.format = None

    def __str__(self):
        return f"{self.title} by {self.author}, Price: {self.price}, Genre: {self.genre}, Format: {self.format}"

# Book Builder
class BookBuilder:
    def __init__(self):
        self.book = Book()

    def add_title(self, title):
        self.book.title = title
        return self

    def add_author(self, author):
        self.book.author = author
        return self

    def add_price(self, price):
        self.book.price = price
        return self

    def add_genre(self, genre):
        self.book.genre = genre
        return self

    def add_format(self, format):
        self.book.format = format
        return self

    def build(self):
        return self.book

# Example usage of the builder pattern
builder = BookBuilder()
book = builder.add_title("The Great Gatsby").add_author("F. Scott Fitzgerald").add_price(19.99).build()
print(book)
