# Online-Bookstore

This project aims to create a simple online platform for small bookstores to sell their books.

## Project Description

The Simple Online Bookstore provides a platform where customers can browse, search, and purchase books online. It focuses on core e-commerce functionalities, allowing small bookstores to expand their customer reach.

## Links

* [SPECIFICATION.md](SPECIFICATION.md)
* [ARCHITECTURE.md](ARCHITECTURE.md)
* [Stakeholder-Analysis.md](Stakeholder-Analysis.md)
* [System-requirements.md](System-requirements.md)
* [Test Cases.md](Test-Cases.md)
* [Use Case Diagram.md](Use-Case-Diagram.md)
* [Use Case Specifications.md](Use-Case-Specifications.md)
* [System-requirements.md](System-requirements.md)
* [Activity_diagrams](Activity_diagrams)
* [Activity_diagrams.md](Activity_diagrams.md)
* [State_transition_diagrams](State_transition_diagrams)
* [State_Transition_Diagrams.md](State_Transition_Diagrams.md)
* 

# 📚 Online Bookstore - Assignment 11: Persistence Repository Layer

## 🚀 Implementation Overview
I've implemented a **repository layer** with full **storage abstraction** for the Online Bookstore system, featuring:

### 🔑 Key Components
1. **Repository Interfaces**
   - Generic `Repository[T, ID]` with CRUD operations.
   - Entity-specific `BookRepository` interface.

2. **Storage Implementations**
   - `InMemoryBookRepository` (HashMap-based in-memory storage).
   - `FileSystemBookRepository` (JSON file-based persistence).

3. **Abstraction Mechanism**
   - `RepositoryFactory` pattern for dynamic storage switching.

✅ Running Tests
# Run all tests with coverage
pytest --cov=online_bookstore.repositories

# Run a specific test file
pytest tests/repositories/inmemory/test_book_repository.py -v

📸 Demo Execution
python demo.py

🔮 Future Extensions
🗄️ Database Support
SQL databases (PostgreSQL, SQLite)

NoSQL databases (MongoDB)

🚀 Enhanced Features
Pagination

Caching layer

Bulk operations (batch save, batch delete)

📈 UML Class Diagram

classDiagram
    class Book

    classDiagram
    class Book

    class BookRepository {
        <<interface>>
        +save(Book)
        +find_by_id(str) Book
        +find_all() List[Book]
        +delete(str)
    }

    BookRepository <|-- InMemoryBookRepository
    BookRepository <|-- FileSystemBookRepository
    RepositoryFactory --> BookRepository

📊 Test Coverage Report

----------- coverage: platform win32, python 3.11.9-final-0 -----------
Name                                               Stmts   Miss  Cover
-----------------------------------------------------------------------
online_bookstore/repositories/__init__.py              0      0   100%
online_bookstore/repositories/book_repository.py       5      0   100%
online_bookstore/repositories/repository.py           10      0   100%
online_bookstore/repositories/filesystem/...          29      0   100%
online_bookstore/repositories/inmemory/...            23      0   100%
-----------------------------------------------------------------------
TOTAL                                                  67      0   100%


## [Assignment 12] - Service Layer and REST API

### Added
- BookService, UserService, and OrderService to handle business logic
- REST API endpoints for `/api/books`, `/api/users`, `/api/orders`
- Swagger UI auto-generated docs at `/docs`
- OpenAPI schema export to `/docs/openapi.json`

  # Triggering GitHub Actions test


### Fixed
- Enforced rule: Users cannot borrow more than 5 books
- Input validation for book creation

### Known Issues
- Checkout currently does not check for overdue books 
