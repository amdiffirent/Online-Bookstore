# 1. Book Object Lifecycle (book_state)

## States:
- **Available**: Can be purchased
- **Reserved**: Temporary hold (e.g., during checkout)
- **InCart**: Added to a shopping cart
- **Purchased**: Successfully sold

## Key Transitions:
- `reserve()`: Holds item for 10 minutes during checkout
- `addToCart()`: Moves to cart until purchase/removal
- `checkout()`: Final purchase confirmation

## Business Rules:
- Items can't be reserved if already in another cart
- Purchased items are archived after 90 days

# 2. User Account States (user_state)

## State Logic:
- **Unverified**: Can browse but not purchase
- **Active**: Full access
- **Suspended**: Temporary restriction (failed payments)
- **Banned**: Permanent removal

## Triggers:
- Automatic suspension after 3 failed payments
- Manual ban for policy violations
- Email verification required for activation

## Related FR:
- FR-101: User authentication
- FR-205: Account security

# 3. Order Fulfillment Workflow (order_activity)

## Key Steps:
1. Payment validation (3rd party API)
2. Parallel actions:
   - Inventory deduction
   - Shipping label generation
3. Customer notifications

## Error Handling:
- Failed payments auto-cancel within 30min
- Inventory errors trigger restocking

## Swimlanes:
- **Customer**: Initiates order
- **Payment Gateway**: Validates transaction
- **Warehouse**: Handles physical fulfillment

# 4. Shopping Cart Lifecycle (cart_state)

## State Logic:
- **Empty**: No products added
- **Active**: Items in cart
- **CheckingOut**: Payment in progress

## Timeouts:
- Active carts expire after 30min
- CheckingOut state lasts max 10min

## Related Features:
- FR-301: Cart persistence
- US-045: Save cart between sessions

# 5. Review Submission Process (review_activity)

## Workflow Rules:
- Only verified purchasers can review
- Auto-approval if no profanity detected
- Manual moderation for 1-star reviews

## Quality Controls:
- Minimum 20 character requirement
- Maximum 1 review per product per user

## Stakeholder Needs:
- Customers want genuine reviews
- Sellers need fraud prevention

# 6. Payment Object States (payment_state)

## Lifecycle:
- **Pending**: Authorization requested
- **Completed**: Funds captured
- **Failed**: Declined/expired
- **Refunded**: Money returned

## Security:
- 5min timeout for pending payments
- Max 3 retry attempts
- Refunds process within 3-5 business days

## Audit Requirements:
- All state changes logged
- No direct state jumps (e.g., Pending→Refunded)


# 7. Inventory Restocking Workflow (inventory_activity)

## Key Stages:
1. Automatic trigger at 10% stock threshold
2. Purchase order generation
3. Two-stage receiving process

## Exception Handling:
- Supplier fallback system
- Automated return processing
- Manager alerts for critical lows

## Integration Points:
- Connected to:
  - Supplier API
  - Warehouse management
  - Financial system

# 8. Product Return Workflow (return_activity)

## Policy Enforcement:
- Strict 30-day window
- Original packaging required
- Restocking fee for damaged items

## Automation:
- Instant label generation
- Refund processing within 1hr of approval
- SMS notifications at each stage

## Fraud Prevention:
- Pattern detection for serial returners
- Manual review for high-value items

