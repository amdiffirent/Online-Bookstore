# tests/test_singleton.py
import unittest
from Assignment_10.creational_patterns.singleton import DatabaseConnection
from Assignment_10.creational_patterns.abstract_factory import BookstoreFactory, BookFactory, AuthorFactory
#from creational_patterns.abstract_factory import BookstoreFactory, BookFactory, AuthorFactory


class TestSingletonPattern(unittest.TestCase):

    def test_singleton_database_connection(self):
        instance1 = DatabaseConnection.get_instance()
        instance2 = DatabaseConnection.get_instance()
        
        # Check if both instances are the same (singleton)
        self.assertIs(instance1, instance2, "Both instances should be the same")

    def test_singleton_thread_safety(self):
        import threading
        
        def create_instance():
            return DatabaseConnection.get_instance()

        # Running in multiple threads to check thread-safety
        threads = [threading.Thread(target=create_instance) for _ in range(10)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        
        # Ensure all threads received the same instance
        instance1 = DatabaseConnection.get_instance()
        instance2 = DatabaseConnection.get_instance()
        self.assertIs(instance1, instance2, "Instances should be the same across threads")

if __name__ == '__main__':
    unittest.main()
