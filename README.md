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

# 📚 Assignment 11: Persistence Repository Layer

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

### Run a specific test file
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

## 📊 Test Coverage Report

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


# Assignment 12 - Service Layer and REST API

### Added
- BookService, UserService, and OrderService to handle business logic
- REST API endpoints for `/api/books`, `/api/users`, `/api/orders`
- Swagger UI auto-generated docs at `/docs`
- OpenAPI schema export to `/docs/openapi.json`

### Fixed
- Enforced rule: Users cannot borrow more than 5 books
- Input validation for book creation

### Known Issues
- Checkout currently does not check for overdue books


# 📚 Assignment 13: CI/CD with GitHub Actions

## 🎯 Objective

This assignment focused on implementing **Continuous Integration (CI)** and **Continuous Deployment (CD)** for the Online Bookstore project using **GitHub Actions**. The goal was to automate the testing process, enforce branch protection, and generate release artifacts when changes are merged into the `main` branch.

---

## 🔒 Branch Protection Rules

I configured **branch protection** rules on the `main` branch to:

- Prevent force pushes and deletions
- Require all commits to go through Pull Requests (PRs)
- Require at least one approval before merging
- Require all status checks (CI tests) to pass before merging

These rules ensure the integrity, stability, and security of the main codebase.

---

## ✅ CI Workflow

I created a CI workflow located at: .github/workflows/ci.yml
This workflow:
- Runs automatically on `push` and `pull_request` events
- Sets up Python
- Installs dependencies using `setup.py` or `requirements.txt`
- Runs all unit tests using `pytest`
- Blocks merging if tests fail

### Example CI Steps:
``yaml
- uses: actions/setup-python@v4
  with:
    python-version: '3.11'

- name: Install dependencies
  run: pip install -e . && pip install pytest

- name: Run tests
  run: pytest 

## 📦 CD Workflow (Release Artifact)
As part of CD, I configured the workflow to:

Run only when changes are pushed to the main branch

Build a distributable Python package using setuptools

Upload the package as an artifact using actions/upload-artifact


## 🔁 Pull Request Workflow
To follow best practices:

All changes are made on a feature branch

A Pull Request is submitted and reviewed

CI must pass and the PR must be approved before merging

Merging generates a release artifact if the base is main

## 🧠 Reflection
Through this assignment, I learned how to:

Enforce safe collaboration using GitHub branch protection

Set up CI to automatically run tests

Create CD pipelines that generate deployable artifacts

Use GitHub Actions effectively for automation


