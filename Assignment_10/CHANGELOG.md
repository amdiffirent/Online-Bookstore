# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2025-04-18
### Added
- Implemented **Simple Factory Pattern** to create different types of Book objects.
- Implemented **Factory Method Pattern** with a PaymentProcessorFactory supporting credit and PayPal processors.
- Implemented **Abstract Factory Pattern** to generate related objects: Books and Authors via BookstoreFactory.
- Implemented **Builder Pattern** to construct complex Book objects with title, author, ISBN, and publisher.
- Implemented **Prototype Pattern** to clone Book objects using ShapeCache with Circle and Rectangle examples.
- Implemented **Singleton Pattern** to manage a single instance of DatabaseConnection.

### Testing
- Added unit tests for each creational pattern:
  - Verified object creation and initialization.
  - Covered edge cases, such as invalid inputs and Singleton thread safety.
- Configured test environment with `pytest` and `pytest-cov`.
- Generated test coverage report for all patterns.

### Project Management
- Updated GitHub Project Board:
  - Moved all implementation and test tasks to **Done**.
  - Linked issues and commits where applicable.
- Created this changelog to document progress.

