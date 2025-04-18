# src/cart.py

class Cart:
    def __init__(self, cart_id, created_at):
        self.__cart_id = cart_id
        self.__created_at = created_at
        self.__items = []

    def add_item(self, book):
        self.__items.append(book)
        print(f"{book.get_title()} added to cart.")

    def remove_item(self, book):
        if book in self.__items:
            self.__items.remove(book)
            print(f"{book.get_title()} removed from cart.")

    def checkout(self):
        print("Checking out...")
        return self.__items

    def get_items(self):
        return self.__items
