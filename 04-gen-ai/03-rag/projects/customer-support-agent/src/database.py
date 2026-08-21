"""SQLite database queries for customer and order data."""

import sqlite3

DB_PATH = "data/support.db"


def get_connection():
    """Get SQLite connection."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Return rows as dicts
    return conn


def get_customer(customer_id: str) -> dict | None:
    """Get customer by ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers WHERE customer_id = ?", (customer_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None


def get_customer_by_email(email: str) -> dict | None:
    """Get customer by email."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers WHERE email = ?", (email,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None


def get_order(order_id: str) -> dict | None:
    """Get order by ID with items."""
    conn = get_connection()
    cursor = conn.cursor()

    # Get order
    cursor.execute("SELECT * FROM orders WHERE order_id = ?", (order_id,))
    order = cursor.fetchone()

    if not order:
        conn.close()
        return None

    order_dict = dict(order)

    # Get items
    cursor.execute(
        "SELECT sku, name, qty, price FROM order_items WHERE order_id = ?", (order_id,)
    )
    order_dict["items"] = [dict(row) for row in cursor.fetchall()]

    conn.close()
    return order_dict


def get_customer_orders(customer_id: str) -> list[dict]:
    """Get all orders for a customer."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM orders WHERE customer_id = ? ORDER BY order_date DESC",
        (customer_id,),
    )
    orders = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return orders


def get_recent_orders(days: int = 30) -> list[dict]:
    """Get recent orders (last N days)."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM orders WHERE order_date >= date('now', '-' || ? || ' days')",
        (days,),
    )
    orders = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return orders


def get_pending_returns() -> list[dict]:
    """Get orders with pending returns."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM orders WHERE return_initiated IS NOT NULL AND refund_status != 'completed'"
    )
    orders = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return orders


def search_customers(query: str) -> list[dict]:
    """Search customers by name or email."""
    conn = get_connection()
    cursor = conn.cursor()
    search_term = f"%{query}%"
    cursor.execute(
        "SELECT * FROM customers WHERE name LIKE ? OR email LIKE ? OR customer_id LIKE ?",
        (search_term, search_term, search_term),
    )
    results = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return results


def get_order_status(order_id: str) -> str | None:
    """Get order status."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT status FROM orders WHERE order_id = ?", (order_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None


def get_customer_tier(customer_id: str) -> str | None:
    """Get customer membership tier."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT tier FROM customers WHERE customer_id = ?", (customer_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None


def format_customer_context(customer_id: str) -> str:
    """Format customer info for LLM context."""
    customer = get_customer(customer_id)
    if not customer:
        return f"Customer {customer_id} not found"

    orders = get_customer_orders(customer_id)
    recent_order = orders[0] if orders else None

    context = f"""
        Customer Information:
        - Name: {customer["name"]}
        - Tier: {customer["tier"]}
        - Account Status: {customer["account_status"]}
        - Member Since: {customer["member_since"]}
        - Total Purchases: {customer["total_purchases"]}
        - Lifetime Value: ${customer["lifetime_value"]:.2f}
        """

    if recent_order:
        context += f"""

        Recent Order:
        - Order ID: {recent_order["order_id"]}
        - Order Date: {recent_order["order_date"]}
        - Order Status: {recent_order["status"]}
        - Amount: ${recent_order["total_amount"]:.2f}
        - Deliver Date: {recent_order["delivery_date"]}
        - Payment Method: {recent_order["payment_method"]}
        """

    return context

    # - Deliver Date: {recent_order["delivery_date"]}
    # - Payment Method: {recent_order["payment_method"]}


def format_order_context(order_id: str) -> str:
    """Format order info for LLM context."""
    order = get_order(order_id)
    if not order:
        return f"Order {order_id} not found"

    items_str = "\n  ".join(
        [
            f"- {item['name']} (x{item['qty']}) - ${item['price']:.2f}"
            for item in order["items"]
        ]
    )

    context = f"""
        Order Information:
        - Order ID: {order_id}
        - Date: {order["order_date"]}
        - Status: {order["status"]}
        - Total: ${order["total_amount"]:.2f}
        - Shipping: {order["shipping_address"]}
        - Payment: {order["payment_method"]}

        Items:
        {items_str}
        """

    if order["status"] == "delivered":
        context += f"\n- Delivered: {order['delivery_date']}"

    if order["return_initiated"]:
        context += f"\n- Return Initiated: {order['return_initiated']}"
        context += f"\n- Return Reason: {order['return_reason']}"
        context += f"\n- Refund Status: {order['refund_status']}"
        if order["refund_amount"]:
            context += f"\n- Refund Amount: ${order['refund_amount']:.2f}"

    return context
