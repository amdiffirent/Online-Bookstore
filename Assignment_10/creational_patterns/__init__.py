# Assignment_10/creational_patterns/__init__.py
from .abstract_factory import BookstoreFactory
from .simple_factory import BookFactory
from .builder import OrderBuilder
from .prototype import BookCache

__all__ = [
    'BookstoreFactory', 
    'BookFactory',
    'OrderBuilder',
    'BookCache'
]




'''# Assignment_10/creational_patterns/__init__.py
# Keep this minimal - don't try to import things that don't exist yet
# Can be empty or just contain:
__all__ = ['abstract_factory', 'builder', 'factory_method', 'prototype', 'simple_factory', 'singleton']


from .simple_factory import BookFactory
from .factory_method import PaymentProcessorFactory, CreditCardProcessor, PayPalProcessor
from .abstract_factory import WindowsFactory, MacOSFactory
from .builder import BookBuilder
from .prototype import Book as PrototypeBook, ShapeCache
from .singleton import DatabaseConnection'''
