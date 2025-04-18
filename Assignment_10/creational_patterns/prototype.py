import copy

# Book Prototype
class Book:
    def __init__(self, title, author, price, genre, format):
        self.title = title
        self.author = author
        self.price = price
        self.genre = genre
        self.format = format

    def clone(self):
        return copy.deepcopy(self)

# Example usage
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 19.99, "Fiction", "Paperback")
book2 = book1.clone()
book2.title = "1984"
book2.author = "George Orwell"
book2.price = 14.99

print(book1)
print(book2)
