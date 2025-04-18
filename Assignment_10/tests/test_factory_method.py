import unittest
from Assignment_10.creational_patterns.factory_method import PaymentProcessorFactory, PaymentProcessor
from Assignment_10.creational_patterns.abstract_factory import BookstoreFactory, BookFactory, AuthorFactory
#from creational_patterns.abstract_factory import BookstoreFactory, BookFactory, AuthorFactory

class TestFactoryMethod(unittest.TestCase):

    def test_credit_card_processor(self):
        factory = PaymentProcessorFactory()
        processor = factory.create_processor("credit")
        self.assertIsInstance(processor, PaymentProcessor)
        self.assertEqual(processor.process_payment(100), "Processing credit card payment of $100")

    def test_paypal_processor(self):
        factory = PaymentProcessorFactory()
        processor = factory.create_processor("paypal")
        self.assertIsInstance(processor, PaymentProcessor)
        self.assertEqual(processor.process_payment(150), "Processing PayPal payment of $150")

    def test_invalid_processor(self):
        factory = PaymentProcessorFactory()
        with self.assertRaises(ValueError):
            factory.create_processor("bitcoin")

if __name__ == '__main__':
    unittest.main()
