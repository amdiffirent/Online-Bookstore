# 📘 Reflection: Domain Modeling and Class Diagram Development

## 1. Challenges I Faced

### Figuring Out the Right Classes
At first, I struggled with how to group everything. For example, I wasn’t sure if I should make the cart a full-on class or just part of the user. I ended up going with a class because it felt more flexible and realistic, especially if the cart had its own data and functions.

### Making the Relationships Work
It took some time to figure out how everything should be connected. I had to think about how users, books, orders, and reviews all link together. Some connections were tricky, especially getting the multiplicity right (like “one user can place many orders”). Mermaid.js also gave me some issues at first when trying to show these connections properly.

### Where Do the Methods Go?
Placing methods in the right classes wasn’t as easy as I thought. For instance, should `processPayment()` live in `Order` or `Payment`? I chose `Order` since it kind of controls the whole checkout process. I tried to keep each class responsible only for its own stuff.

## 2. How It Links to Previous Work

### Functional Requirements & Use Cases
I tried to stick closely to the earlier assignments. For example:
- FR-001 (registering users) → matches `User.register()`
- FR-005 (cancelling an order) → represented by `Order.cancelOrder()`
- UC-004 (reviewing a book) → shows up with the `Review` class connected to both `User` and `Book`

### State & Activity Diagrams
This diagram also builds on the activity and state diagrams from Assignment 8. Stuff like checking out and returning a book matches with `Book.checkOut()` and `Book.returnBook()`. The overall flow — from adding to cart to placing an order — is also supported by the classes I created.

## 3. Trade-Offs I Made

### Inheritance
I didn’t want to over-complicate things with too many inheritance layers. The only one I used was between `User` and `Admin`, which made sense because they share some features. In other places, like with `Cart` holding books, I stuck to composition.

### Keeping It Simple (But Not Too Simple)
I could’ve gone deeper with certain classes — like having different payment types or statuses — but I chose to keep it general with a `validate()` method to keep the focus on core functionality.

## 4. What I Learned

### Better OOP Thinking
This task helped me think more like a developer:
- I got better at keeping class responsibilities separate.
- I started paying more attention to encapsulation — using private fields and exposing actions through methods.
- I now understand how a clean design helps everyone — not just developers, but users and stakeholders too.


