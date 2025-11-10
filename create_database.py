import pandas as pd
from sqlalchemy import create_engine, text
import os

print("=" * 60)
print("DATABASE SETUP (SQLite)")
print("=" * 60)

# Create database connection (SQLite - no installation needed!)
db_path = 'ecommerce_analytics.db'
engine = create_engine(f'sqlite:///{db_path}')

print(f"\n📊 Creating SQLite database: {db_path}")
print("   (SQLite requires zero setup - works instantly!)")

# Load CSV files
print("\n📂 Loading CSV files...")

try:
    customers = pd.read_csv('data/customers.csv')
    orders = pd.read_csv('data/orders.csv')
    products = pd.read_csv('data/products.csv')
    order_items = pd.read_csv('data/order_items.csv')
    print("✅ CSV files loaded successfully")
except FileNotFoundError as e:
    print(f"❌ Error: {e}")
    print("   Make sure you've run generate_sample_data.py first!")
    exit(1)

# Write to database
print("\n💾 Writing tables to database...")

customers.to_sql('customers', engine, if_exists='replace', index=False)
print("   ✅ customers table created")

orders.to_sql('orders', engine, if_exists='replace', index=False)
print("   ✅ orders table created")

products.to_sql('products', engine, if_exists='replace', index=False)
print("   ✅ products table created")

order_items.to_sql('order_items', engine, if_exists='replace', index=False)
print("   ✅ order_items table created")

# Verify
print("\n🔍 Verifying database...")
with engine.connect() as conn:
    result = conn.execute(text("SELECT COUNT(*) FROM orders"))
    order_count = result.fetchone()[0]

    result = conn.execute(text("SELECT COUNT(*) FROM customers"))
    customer_count = result.fetchone()[0]

    result = conn.execute(text("SELECT COUNT(*) FROM products"))
    product_count = result.fetchone()[0]

    result = conn.execute(text("SELECT COUNT(*) FROM order_items"))
    item_count = result.fetchone()[0]

print(f"\n✅ Database created successfully!")
print(f"\n📊 Records in database:")
print(f"   • Customers: {customer_count:,}")
print(f"   • Orders: {order_count:,}")
print(f"   • Products: {product_count:,}")
print(f"   • Order Items: {item_count:,}")

db_size = os.path.getsize(db_path) / (1024 * 1024)  # Convert to MB
print(f"\n📁 Database file: {os.path.abspath(db_path)}")
print(f"   Size: {db_size:.2f} MB")

print("\n🔍 You can now run SQL queries using sql_queries.py!")

# Create a simple query example
print("\n" + "=" * 60)
print("SAMPLE QUERY - Top 5 Customers by Revenue")
print("=" * 60)

sample_query = """
               SELECT customer_id, \
                      COUNT(order_id)             AS total_orders, \
                      ROUND(SUM(total_amount), 2) AS total_spent
               FROM orders
               WHERE order_status = 'Completed'
               GROUP BY customer_id
               ORDER BY total_spent DESC LIMIT 5; \
               """

top_customers = pd.read_sql(sample_query, engine)
print("\n" + top_customers.to_string(index=False))

print("\n" + "=" * 60)
print("✅ Database Setup Complete!")
print("\n💡 To view/query the database:")
print("   • Use sql_queries.py (next step)")
print("   • Or install DB Browser for SQLite (free GUI tool)")
print("   • Or use PyCharm's Database tool (View → Tool Windows → Database)")
print("=" * 60)