# src/payment.py

class Payment:
    def __init__(self, payment_id, amount, payment_method, status="Pending"):
        self.__payment_id = payment_id
        self.__amount = amount
        self.__payment_method = payment_method
        self.__status = status

    def validate(self):
        # Simulate a successful validation
        if self.__amount > 0:
            self.__status = "Validated"
            print("Payment validated.")
            return True
        print("Invalid payment amount.")
        return False

    def refund(self):
        if self.__status == "Validated":
            self.__status = "Refunded"
            print("Payment refunded.")
            return True
        print("Cannot refund unless payment is validated.")
        return False

    def get_status(self):
        return self.__status
