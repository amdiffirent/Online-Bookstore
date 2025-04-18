from .simple_factory import BookFactory
from .factory_method import PaymentProcessorFactory, CreditCardProcessor, PayPalProcessor
from .abstract_factory import WindowsFactory, MacOSFactory
from .builder import BookBuilder
from .prototype import Book as PrototypeBook, ShapeCache
from .singleton import DatabaseConnection
