# Customer Support Agent (Week 4 - Naive RAG)

A retrieval-augmented generation system for customer support queries in e-commerce.

## Dataset Overview

### Customer Data (`data/customers.json`)
- 5 sample customers with varying membership tiers
- Fields: ID, name, email, phone, account status, membership info, purchase history
- Used for: Personalizing responses, checking account status, verifying customer identity

### Order Data (`data/orders.json`)
- 5 sample orders with complete lifecycle (processing, shipped, delivered, returned)
- Fields: Order ID, items, status, dates, shipping info, payment method, refund status
- Used for: Order tracking, return processing, refund inquiries

### Policy Documentation (`data/policies.md`)
Comprehensive company policies covering:
- **Return & Refund Policy**: 30-90 day windows, eligibility, process, non-returnable items
- **Shipping Policy**: Delivery times, costs, restrictions, international shipping
- **Warranty**: 1-year standard, extended warranties, claims process
- **Payment & Security**: Methods, payment plans, fraud protection
- **Customer Service**: Support hours, response times, loyalty tiers
- **Privacy & ToS**: Data protection, account responsibilities, prohibited activities

### FAQs (`data/faqs.md`)
Pre-written answers to ~30 common customer questions across:
- Shipping & Delivery
- Returns & Refunds
- Payments & Billing
- Products & Orders
- Account & Loyalty
- Contact Information

---

## Use Cases for Week 4 RAG Implementation

### 1. **Query Resolution**
```
Customer: "What's your return policy?"
Agent: Retrieves from policies.md → Formats answer → Responds
```

### 2. **Order Lookup**
```
Customer: "Where's my order ORD-2024-001?"
Agent: Queries orders.json → Finds tracking info → Provides status
```

### 3. **Account-Specific Questions**
```
Customer: "What's my loyalty tier?"
Agent: Queries customers.json → Retrieves tier → Provides discount info
```

### 4. **FAQ Matching**
```
Customer: "Do you accept PayPal?"
Agent: Retrieves from FAQs → Finds answer → Provides direct response
```

### 5. **Complex Scenarios**
```
Customer: "Can I return my order from 45 days ago?"
Agent: 
  1. Retrieves order date from orders.json
  2. Checks policy from policies.md (30-day window)
  3. Asks about defect (extends to 90 days)
  4. Provides personalized answer
```

---

## How to Use This Data

### Option 1: Direct JSON Queries
```python
import json

# Load customer data
with open("data/customers.json") as f:
    customers = json.load(f)

# Look up customer
customer = next(c for c in customers if c["customer_id"] == "CUST001")
print(f"Tier: {customer['tier']}")
```

### Option 2: Embed as Documents (RAG Pipeline)
```python
# Convert to documents for embedding
documents = []

# Add policy sections
with open("data/policies.md") as f:
    policy_text = f.read()
    # Split by section, embed each

# Add FAQs
with open("data/faqs.md") as f:
    faq_text = f.read()
    # Split by Q&A, embed each

# Add structured data as text
for customer in customers:
    doc = f"Customer {customer['customer_id']}: {customer['name']}, Tier: {customer['tier']}"
    documents.append(doc)
```

### Option 3: Hybrid Approach (Recommended)
- **RAG for**: Policies, FAQs, general knowledge
- **Database for**: Customer lookups, order status (structured queries are better)
- **Hybrid**: Customer asks about order → retrieve order from DB → add to context → generate response

---

## Data Statistics

| Category | Count | Notes |
|----------|-------|-------|
| Customers | 5 | 1 suspended, tiers: bronze-platinum |
| Orders | 5 | 1 processing, 1 shipped, 2 delivered, 1 returned |
| Policies | 6 sections | ~2000 words total |
| FAQs | 30+ questions | ~2000 words |

---

## Extending the Dataset

### Add More Customers
```json
{
  "customer_id": "CUST006",
  "name": "New Customer",
  "tier": "bronze",
  "account_status": "active",
  ...
}
```

### Add More Orders
```json
{
  "order_id": "ORD-2024-006",
  "customer_id": "CUST001",
  "status": "processing",
  ...
}
```

### Add More Policy Sections
Edit `policies.md` to add sections for:
- Corporate/bulk orders
- Gift cards
- Subscriptions
- B2B policies
- Financing options

---

## Week 4 Implementation Plan

1. **Load all data** into embeddings/ChromaDB (like research-agent)
2. **Create RAG pipeline** to retrieve relevant context
3. **Build response formatter** to handle different query types
4. **Implement agent loop** that:
   - Takes customer query
   - Retrieves relevant documents
   - Combines with customer/order context
   - Generates response via LLM
5. **Test scenarios** (returns, payments, shipping, account issues)

This dataset supports all of Week 4's learning objectives.
