import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

print("🔄 Generating sample e-commerce data...")

# Generate 60,000 orders
n_orders = 60000
n_customers = 15000
n_products = 500

# Date range: Jan 2023 - May 2025
start_date = datetime(2023, 1, 1)
end_date = datetime(2025, 5, 31)
date_range = (end_date - start_date).days

# Customers table
print("Creating customers table...")
customers = pd.DataFrame({
    'customer_id': range(1, n_customers + 1),
    'signup_date': [start_date + timedelta(days=int(np.random.random() * date_range)) for _ in range(n_customers)],
    'location': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Boston', 'Seattle'], n_customers),
    'age_group': np.random.choice(['18-25', '26-35', '36-45', '46-55', '55+'], n_customers, p=[0.2, 0.3, 0.25, 0.15, 0.1])
})

# Orders table
print("Creating orders table...")
# Some customers buy more (80/20 rule)
repeat_customers = np.random.choice(customers['customer_id'].values[:3000], size=int(n_orders*0.6))
new_customers = np.random.choice(customers['customer_id'].values, size=int(n_orders*0.4))
all_customer_ids = np.concatenate([repeat_customers, new_customers])

orders = pd.DataFrame({
    'order_id': range(1, n_orders + 1),
    'customer_id': all_customer_ids,
    'order_date': [start_date + timedelta(days=int(np.random.exponential(scale=date_range/2))) for _ in range(n_orders)],
    'total_amount': np.random.gamma(shape=2, scale=50, size=n_orders).round(2),
    'order_status': np.random.choice(['Completed', 'Pending', 'Cancelled'], n_orders, p=[0.85, 0.10, 0.05])
})

# Clip dates to valid range
orders['order_date'] = orders['order_date'].clip(upper=end_date)

# Products table
print("Creating products table...")
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Beauty & Personal Care', 'Sports & Outdoors', 'Books', 'Toys & Games']
products = pd.DataFrame({
    'product_id': range(1, n_products + 1),
    'product_name': [f'Product_{i:04d}' for i in range(1, n_products + 1)],
    'category': np.random.choice(categories, n_products),
    'cost_price': np.random.uniform(10, 100, n_products).round(2),
    'retail_price': np.random.uniform(20, 200, n_products).round(2),
    'current_stock': np.random.randint(0, 500, n_products)
})

# Ensure retail > cost
products['retail_price'] = products.apply(lambda row: max(row['retail_price'], row['cost_price'] * 1.3), axis=1).round(2)

# Order Items table
print("Creating order_items table...")
order_items = pd.DataFrame({
    'item_id': range(1, n_orders + 1),
    'order_id': range(1, n_orders + 1),
    'product_id': np.random.choice(products['product_id'], n_orders),
    'quantity': np.random.choice([1, 2, 3], n_orders, p=[0.7, 0.2, 0.1]),
    'unit_price': np.random.uniform(20, 200, n_orders).round(2),
    'discount_amount': np.random.choice([0, 5, 10, 15, 20], n_orders, p=[0.5, 0.2, 0.15, 0.1, 0.05])
})

# Save to CSV files
print("\n💾 Saving files...")
customers.to_csv('data/customers.csv', index=False)
orders.to_csv('data/orders.csv', index=False)
products.to_csv('data/products.csv', index=False)
order_items.to_csv('data/order_items.csv', index=False)

# Print summary
print("\n✅ DATA GENERATION COMPLETE!\n")
print(f"📊 Summary:")
print(f"   • Customers: {len(customers):,}")
print(f"   • Orders: {len(orders):,}")
print(f"   • Products: {len(products):,}")
print(f"   • Order Items: {len(order_items):,}")
print(f"   • Date Range: {orders['order_date'].min().date()} to {orders['order_date'].max().date()}")
print(f"   • Total Revenue: ${orders['total_amount'].sum():,.2f}")
print(f"\n📁 Files saved in: data/ folder")