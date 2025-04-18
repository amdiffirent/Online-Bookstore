class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def connect(self):
        return "Connected to database"

# Usage example
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1.connect())
print(db1 is db2)  # True, both are the same instance
