# src/order.py

class Order:
    def __init__(self, order_id, order_date, books, total_amount, status="Pending"):
        self.__order_id = order_id
        self.__order_date = order_date
        self.__books = books  # Expecting a list of Book instances
        self.__total_amount = total_amount
        self.__status = status

    def process_payment(self):
        if self.__status == "Pending":
            self.__status = "Paid"
            print("Payment processed.")
            return True
        return False

    def cancel_order(self):
        if self.__status == "Pending":
            self.__status = "Cancelled"
            print("Order cancelled.")
            return True
        return False

    def get_status(self):
        return self.__status

    def get_books(self):
        return self.__books
