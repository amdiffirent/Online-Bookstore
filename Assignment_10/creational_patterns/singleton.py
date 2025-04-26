# Assignment_10/creational_patterns/singleton.py
import threading

class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    # Initialize connection here
                    cls._instance.connection = "Active DB Connection"
        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()

    def __str__(self):
        return "DatabaseConnection"
    