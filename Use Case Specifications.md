## Use Case Specifications

### Use Case 1: Search Books
- **Actor**: Customer
- **Description**: Allows customers to search for books by title, author, or ISBN.
- **Preconditions**: The customer is logged in and the system is online.
- **Postconditions**: Search results are displayed, and book availability is updated.
- **Basic Flow**:
  1. Customer enters search criteria (title, author, or ISBN).
  2. System validates the input.
  3. System queries the database.
  4. System displays search results with real-time availability.
- **Alternative Flows**:
  - **No Results Found**: System displays "No matches found."
  - **Invalid Input**: System prompts the customer to re-enter search criteria.

### Use Case 2: Add to Cart
- **Actor**: Customer
- **Description**: Allows customers to add books to their shopping cart.
- **Preconditions**: The customer is logged in and has searched for a book.
- **Postconditions**: The book is added to the cart, and the cart total is updated.
- **Basic Flow**:
  1. Customer selects a book from search results.
  2. Customer clicks "Add to Cart."
  3. System updates the cart and displays the updated total.
- **Alternative Flows**:
  - **Out of Stock**: System notifies the customer that the book is unavailable.
  - **Duplicate Item**: System updates the quantity of the existing item in the cart.

### Use Case 3: Process Checkout
- **Actor**: Customer
- **Description**: Allows customers to complete their purchase.
- **Preconditions**: The customer has items in their cart and is logged in.
- **Postconditions**: The order is confirmed, and inventory is updated.
- **Basic Flow**:
  1. Customer proceeds to checkout.
  2. System validates the cart contents.
  3. System prompts for payment details.
  4. System processes the payment.
  5. System confirms the order and updates inventory.
- **Alternative Flows**:
  - **Payment Failed**: System prompts the customer to retry payment.
  - **Out of Stock**: System notifies the customer and removes the item from the cart.

### Use Case 4: Manage Inventory
- **Actor**: Bookstore Owner
- **Description**: Allows the bookstore owner to add, update, or remove books from the inventory.
- **Preconditions**: The bookstore owner is logged in and has admin privileges.
- **Postconditions**: Inventory is updated, and changes are reflected in real time.
- **Basic Flow**:
  1. Bookstore owner selects "Manage Inventory."
  2. System displays current inventory.
  3. Owner adds, updates, or removes a book.
  4. System updates the database.
- **Alternative Flows**:
  - **Invalid Data**: System prompts the owner to correct the input.
  - **Database Error**: System displays an error message and logs the issue.

### Use Case 5: Leave Review
- **Actor**: Customer
- **Description**: Allows customers to leave reviews and ratings for purchased books.
- **Preconditions**: The customer has purchased the book and is logged in.
- **Postconditions**: The review is posted, and the book’s average rating is updated.
- **Basic Flow**:
  1. Customer selects "Leave Review."
  2. System prompts for a rating and review text.
  3. Customer submits the review.
  4. System validates and posts the review.
- **Alternative Flows**:
  - **Inappropriate Content**: System flags the review for moderation.
  - **Duplicate Review**: System notifies the customer that they’ve already reviewed the book.

### Use Case 6: Apply Discount
- **Actor**: Customer
- **Description**: Allows customers to apply discount or promo codes during checkout.
- **Preconditions**: The customer has items in their cart and is logged in.
- **Postconditions**: The discount is applied, and the cart total is updated.
- **Basic Flow**:
  1. Customer enters a promo code during checkout.
  2. System validates the promo code.
  3. System applies the discount to the cart total.
- **Alternative Flows**:
  - **Invalid Promo Code**: System notifies the customer that the code is invalid.
  - **Expired Promo Code**: System notifies the customer that the code has expired.

### Use Case 7: Track Order
- **Actor**: Customer
- **Description**: Allows customers to track the status of their orders.
- **Preconditions**: The customer has placed an order and is logged in.
- **Postconditions**: The order status is displayed.
- **Basic Flow**:
  1. Customer selects "Track Order."
  2. System retrieves the order status from the database.
  3. System displays the order status (e.g., "Shipped," "Out for Delivery").
- **Alternative Flows**:
  - **Order Not Found**: System notifies the customer that the order does not exist.
  - **Delivery Delayed**: System displays an estimated delay in delivery.

### Use Case 8: View Sales Reports
- **Actor**: Bookstore Owner
- **Description**: Allows the bookstore owner to view sales reports.
- **Preconditions**: The bookstore owner is logged in and has admin privileges.
- **Postconditions**: The sales report is displayed.
- **Basic Flow**:
  1. Bookstore owner selects "View Sales Reports."
  2. System retrieves sales data from the database.
  3. System generates and displays the sales report.
- **Alternative Flows**:
  - **No Data Available**: System notifies the owner that no sales data is available.
  - **Database Error**: System displays an error message and logs the issue.
