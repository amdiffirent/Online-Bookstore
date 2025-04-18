# Creational Pattern Implementations – Online Bookstore

---

## ✅ Simple Factory

**Use Case:** Book creation (Paperback, Ebook, Audiobook)

**Justification:** A centralized `BookFactory` simplifies the creation of different book formats without exposing the instantiation logic to the client.

---

## ✅ Factory Method

**Use Case:** Payment processing (Credit Card, PayPal)

**Justification:** Payment types vary and new processors may be added later. Using a factory method allows easy extension and decouples the logic for processing payments.

---

## ✅ Abstract Factory

**Use Case:** UI Component rendering (Windows vs MacOS)

**Justification:** Different platforms (Windows, MacOS) require different UI components. The abstract factory allows consistent creation of platform-specific UI widgets.

---

## ✅ Builder

**Use Case:** Book customization (title, author, price, genre, format)

**Justification:** Some books have optional properties. Using a `BookBuilder` makes it easier to create complex book objects step-by-step without requiring a huge constructor.

---

## ✅ Prototype

**Use Case:** Cloning book templates

**Justification:** To avoid re-initializing book objects repeatedly (e.g., for promotions or templates), we use a prototype pattern to clone existing books efficiently.

---

## ✅ Singleton

**Use Case:** Database connection

**Justification:** There should only be one connection to the database throughout the app. The singleton pattern ensures only one instance of the connection exists.
