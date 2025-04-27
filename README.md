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

## Repository Layer Implementation

- Used generics in `Repository[T, ID]` to avoid duplication across entity repositories
- Implemented in-memory storage using Python dictionaries
- Used Factory pattern to abstract repository creation
- Future storage implementations can be added by:
  1. Creating new repository implementations
  2. Extending the RepositoryFactory

  Class Diagram Additions:

[Book] --> [BookRepository]
[BookRepository] <|-- [InMemoryBookRepository]
[BookRepository] <|-- [FileSystemBookRepository]
[RepositoryFactory] --> [InMemoryBookRepository]
[RepositoryFactory] --> [FileSystemBookRepository]