# src/book.py

class Book:
    def __init__(self, book_id, title, author, genre, price, status="Available"):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__price = price
        self.__status = status

    def check_out(self):
        if self.__status == "Available":
            self.__status = "Checked Out"
            return True
        return False

    def return_book(self):
        if self.__status == "Checked Out":
            self.__status = "Available"
            return True
        return False

    def get_status(self):
        return self.__status

    def get_price(self):
        return self.__price

    def get_title(self):
        return self.__title
