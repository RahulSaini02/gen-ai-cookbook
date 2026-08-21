"""Load customer and order data into SQLite."""

import json
import sqlite3
from pathlib import Path

DB_PATH = "data/support.db"
DATA_DIR = Path("data")


def init_database():
    """Create database schema."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Customers table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            account_status TEXT,
            member_since DATE,
            tier TEXT,
            total_purchases INTEGER,
            lifetime_value REAL,
            suspension_reason TEXT
        )
    """)

    # Orders table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT PRIMARY KEY,
            customer_id TEXT NOT NULL,
            order_date DATE,
            status TEXT,
            total_amount REAL,
            shipping_address TEXT,
            delivery_date DATE,
            payment_method TEXT,
            tracking_number TEXT,
            return_initiated DATE,
            return_reason TEXT,
            refund_status TEXT,
            refund_amount REAL,
            notes TEXT,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    """)

    # Order items table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id TEXT NOT NULL,
            sku TEXT,
            name TEXT,
            qty INTEGER,
            price REAL,
            FOREIGN KEY (order_id) REFERENCES orders(order_id)
        )
    """)

    conn.commit()
    return conn


def load_customers(conn):
    """Load customers from JSON."""
    with open(DATA_DIR / "customers.json") as f:
        customers = json.load(f)

    cursor = conn.cursor()
    for customer in customers:
        cursor.execute("""
            INSERT OR REPLACE INTO customers
            (customer_id, name, email, phone, account_status, member_since,
             tier, total_purchases, lifetime_value, suspension_reason)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            customer.get("customer_id"),
            customer.get("name"),
            customer.get("email"),
            customer.get("phone"),
            customer.get("account_status"),
            customer.get("member_since"),
            customer.get("tier"),
            customer.get("total_purchases"),
            customer.get("lifetime_value"),
            customer.get("suspension_reason"),
        ))

    conn.commit()
    print(f"✓ Loaded {len(customers)} customers")


def load_orders(conn):
    """Load orders from JSON."""
    with open(DATA_DIR / "orders.json") as f:
        orders = json.load(f)

    cursor = conn.cursor()
    for order in orders:
        # Insert order
        cursor.execute("""
            INSERT OR REPLACE INTO orders
            (order_id, customer_id, order_date, status, total_amount,
             shipping_address, delivery_date, payment_method, tracking_number,
             return_initiated, return_reason, refund_status, refund_amount, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            order.get("order_id"),
            order.get("customer_id"),
            order.get("order_date"),
            order.get("status"),
            order.get("total_amount"),
            order.get("shipping_address"),
            order.get("delivery_date"),
            order.get("payment_method"),
            order.get("tracking_number"),
            order.get("return_initiated"),
            order.get("return_reason"),
            order.get("refund_status"),
            order.get("refund_amount"),
            order.get("notes"),
        ))

        # Insert order items
        for item in order.get("items", []):
            cursor.execute("""
                INSERT INTO order_items (order_id, sku, name, qty, price)
                VALUES (?, ?, ?, ?, ?)
            """, (
                order.get("order_id"),
                item.get("sku"),
                item.get("name"),
                item.get("qty"),
                item.get("price"),
            ))

    conn.commit()
    print(f"✓ Loaded {len(orders)} orders")


def main():
    """Initialize and load all data."""
    print("Initializing database...")
    conn = init_database()

    print("Loading customers...")
    load_customers(conn)

    print("Loading orders...")
    load_orders(conn)

    conn.close()
    print(f"✓ Database created at {DB_PATH}")


if __name__ == "__main__":
    main()
