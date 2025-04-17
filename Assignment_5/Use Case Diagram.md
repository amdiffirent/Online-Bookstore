graph TD
    A[Customer] -->|Searches for books| B(Search Books)
    A -->|Adds to cart| C(Add to Cart)
    A -->|Checks out| D(Process Checkout)
    A -->|Leaves review| E(Leave Review)
    F[Bookstore Owner] -->|Manages inventory| G(Manage Inventory)
    F -->|Views sales reports| H(View Sales Reports)
    I[Inventory Manager] -->|Updates stock| G
    J[Payment Gateway Provider] -->|Processes payment| D
    K[Shipping Personnel] -->|Ships orders| L(Ship Order)
    B -->|Includes| M(Check Availability)
    D -->|Extends| N(Apply Discount)
