# 📘 Domain Model - Online Bookstore

This domain model captures the key entities, attributes, methods, and relationships in the Online Bookstore system.

| Entity     | Attributes                               | Methods                              | Relationships                              |
|------------|------------------------------------------|--------------------------------------|--------------------------------------------|
| User       | userId, name, email, password, role      | register(), login(), updateProfile() | Can place many Orders, write Reviews       |
| Book       | bookId, title, author, genre, price, status | checkOut(), returnBook()             | Associated with many Orders and Reviews     |
| Order      | orderId, orderDate, status, totalAmount  | processPayment(), cancelOrder()      | Linked to one User, contains many Books     |
| Cart       | cartId, createdAt                        | addItem(), removeItem(), checkout()  | Belongs to one User, contains many Books    |
| Review     | reviewId, rating, comment, date          | submitReview(), editReview()         | Linked to one User and one Book             |
| Payment    | paymentId, amount, paymentMethod, status | validate(), refund()                 | Linked to one Order                         |
| Admin      | adminId, name, email                     | addBook(), updateInventory(), generateReport() | Inherits from User                |

## 🧾 Business Rules

- A User can place multiple Orders, but an Order belongs to one User.
- A Cart is associated with one User and can contain multiple Books.
- A Book can receive multiple Reviews, but a Review is tied to one Book and one User.
- Only Admin users can add or update book inventory.
- A User can submit one Review per Book.
- Payment must be validated before an Order is marked as 'Completed'.
