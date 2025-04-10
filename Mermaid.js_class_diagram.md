# 🧩 Class Diagram - Online Bookstore (Mermaid.js)

```mermaid
classDiagram
%% ====== User and Admin ======
class User {
  -userId: String
  -name: String
  -email: String
  -password: String
  -role: String
  +register()
  +login()
  +updateProfile()
}

class Admin {
  -adminId: String
  +addBook()
  +updateInventory()
  +generateReport()
}
Admin --|> User

%% ====== Book, Review ======
class Book {
  -bookId: String
  -title: String
  -author: String
  -genre: String
  -price: Float
  -status: String
  +checkOut()
  +returnBook()
}

class Review {
  -reviewId: String
  -rating: Int
  -comment: String
  -date: Date
  +submitReview()
  +editReview()
}
User "1" -- "0..*" Review : writes
Book "1" -- "0..*" Review : has

%% ====== Order, Cart, Payment ======
class Order {
  -orderId: String
  -orderDate: Date
  -status: String
  -totalAmount: Float
  +processPayment()
  +cancelOrder()
}
User "1" -- "0..*" Order : places
Order "1" -- "1..*" Book : contains

class Cart {
  -cartId: String
  -createdAt: Date
  +addItem()
  +removeItem()
  +checkout()
}
User "1" -- "1" Cart : owns
Cart "1" -- "0..*" Book : holds

class Payment {
  -paymentId: String
  -amount: Float
  -paymentMethod: String
  -status: String
  +validate()
  +refund()
}
Payment "1" -- "1" Order : for


