## Test Cases

| Test Case ID | Requirement ID | Description                  | Steps                                                                 | Expected Result                     | Actual Result | Status (Pass/Fail) |
|--------------|----------------|------------------------------|-----------------------------------------------------------------------|-------------------------------------|---------------|--------------------|
| TC-001       | FR-001         | Customer searches for a book | 1. Enter title. 2. Click Search.                                      | Results display within 2 seconds.   |               |                    |
| TC-002       | FR-004         | Customer checks out          | 1. Add items to cart. 2. Proceed to checkout. 3. Enter payment details. | Order is confirmed, inventory updated. |               |                    |
| TC-003       | NFR-001        | Performance test             | Simulate 1,000 concurrent users searching for books.                  | Response time ≤ 2 seconds.          |               |                    |
| TC-004       | NFR-002        | Security test                | Attempt to access admin panel without credentials.                    | Access is denied.                   |               |                    |
| TC-005       | FR-003         | Add to Cart                  | 1. Add a book to the cart. 2. View cart.                              | Book appears in the cart.           |               |                    |
| TC-006       | FR-005         | Manage Inventory             | 1. Log in as bookstore owner. 2. Add a new book.                      | Book is added to inventory.         |               |                    |
| TC-007       | FR-007         | Leave Review                 | 1. Purchase a book. 2. Leave a review.                                | Review is posted.                   |               |                    |
| TC-008       | FR-008         | Apply Discount               | 1. Enter promo code during checkout. 2. Complete purchase.            | Discount is applied to the total.   |               |                    |
