from abc import ABC, abstractmethod

# PaymentProcessor Interface
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# CreditCardProcessor (Concrete Class)
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing credit card payment of R{amount}"

# PayPalProcessor (Concrete Class)
class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing PayPal payment of R{amount}"

# Factory Method
class PaymentProcessorFactory:
    @staticmethod
    def create_processor(payment_method):
        if payment_method == "credit_card":
            return CreditCardProcessor()
        elif payment_method == "paypal":
            return PayPalProcessor()
        else:
            raise ValueError(f"Unknown payment method: {payment_method}")

# Example usage of the factory method
payment_processor = PaymentProcessorFactory.create_processor("credit_card")
print(payment_processor.process_payment(100))
