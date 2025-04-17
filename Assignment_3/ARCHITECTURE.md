# Online Bookstore - Architectural Modeling

## 1. Introduction

* Project Title: Online Bookstore
* Domain: E-commerce, specifically online book sales for independent bookstores.
* Problem Statement: There are many small, independent bookstores that lack an online presence,that limits their ability to reach a wider customer base and compete with larger online retailers. This system aims to provide a simple and accessible platform for them to sell books online, manage inventory, and process orders.
* Individual Scope: This project will focus on the essential functionalities of an online bookstore, including book browsing, searching, user authentication, shopping cart management, and order placement. More complex features like advanced payment integration (using a simplified simulation), detailed shipping tracking, and comprehensive inventory management will be simplified or omitted to ensure the project's feasibility for an individual developer.

## 2. C4 Architectural Diagrams

### 2.1. System Context Diagram

```mermaid
graph LR
    A[Customer] -->|Browses, searches, orders| B(Online Bookstore);
    C[Bookstore Owner] -->|Manages books and orders| B;
    B -->|Processes payment transactions| D[Payment Simulation];
    B -->|Sends shipping information| E[Shipping Service];

## 2.2. Container Diagram


    A[Customer] -->|Uses| B(Web Application);
    F[Bookstore Owner] -->|Manages| B;
    C(Database) <--|Reads from/writes to| B;
    
## 2.3.Component Diagram

    A(Book Controller) --> B(Book Service);
    C(User Controller) --> D(User Service);
    E(Order Controller) --> F(Order Service);
    G(Authentication Controller) --> H(Authentication Service);
    B --> I(Book Repository);
    D --> J(User Repository);
    F --> K(Order Repository);
    H --> J;
    I --> L[Database];
    J --> L;
    K --> L;
