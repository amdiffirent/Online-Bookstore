# Assignment_10/creational_patterns/builder.py
class Order:
    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = []
        self.discount = None
        self.delivery = None
    
    def __str__(self):
        return f"Order[ID={self.order_id}, Customer={self.customer_name}, Items={self.items}, Discount={self.discount}, Delivery={self.delivery}]"

class OrderBuilder:
    def __init__(self, order_id, customer_name):
        self.order = Order(order_id, customer_name)
    
    def add_item(self, name, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.order.items.append((name, quantity))
        return self
    
    def set_discount(self, discount):
        self.order.discount = discount
        return self
    
    def set_delivery(self, delivery):
        self.order.delivery = delivery
        return self
    
    def build(self):
        return self.order






'''# Book class
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
print(book) '''
