# Assignment_10/creational_patterns/factory_method.py
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}"

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing PayPal payment of ${amount}"

class PaymentProcessorFactory:
    @staticmethod
    def create_processor(payment_method):
        if payment_method == "credit":  # Changed from "credit_card" to match test
            return CreditCardProcessor()
        elif payment_method == "paypal":
            return PayPalProcessor()
        else:
            raise ValueError(f"Unknown payment method: {payment_method}")
