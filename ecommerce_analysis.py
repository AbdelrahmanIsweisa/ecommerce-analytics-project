"""
E-Commerce Sales Optimization & Customer Insights
Analyzing 60K+ transactions to identify customer behavior and forecast sales
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', 100)

# Set style for plots
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

print("=" * 60)
print("E-COMMERCE ANALYTICS PROJECT")
print("=" * 60)

# ====================
# 1. LOAD DATA
# ====================
print("\n📂 Loading data...")

customers = pd.read_csv('data/customers.csv')
orders = pd.read_csv('data/orders.csv')
products = pd.read_csv('data/products.csv')
order_items = pd.read_csv('data/order_items.csv')

print(f"✅ Loaded:")
print(f"   • Customers: {len(customers):,} rows")
print(f"   • Orders: {len(orders):,} rows")
print(f"   • Products: {len(products):,} rows")
print(f"   • Order Items: {len(order_items):,} rows")

# ====================
# 2. DATA PREPROCESSING
# ====================
print("\n🔧 Preprocessing data...")

# Convert dates
orders['order_date'] = pd.to_datetime(orders['order_date'])
customers['signup_date'] = pd.to_datetime(customers['signup_date'])

# Check for missing values
print("\n📊 Missing values check:")
print(orders.isnull().sum())

# ====================
# 3. BASIC STATISTICS
# ====================
print("\n" + "=" * 60)
print("KEY METRICS")
print("=" * 60)

total_revenue = orders[orders['order_status'] == 'Completed']['total_amount'].sum()
avg_order_value = orders[orders['order_status'] == 'Completed']['total_amount'].mean()
total_customers = orders['customer_id'].nunique()
total_orders = len(orders[orders['order_status'] == 'Completed'])

print(f"\n💰 Total Revenue: ${total_revenue:,.2f}")
print(f"📦 Total Orders: {total_orders:,}")
print(f"👥 Unique Customers: {total_customers:,}")
print(f"💵 Average Order Value: ${avg_order_value:.2f}")
print(f"🔄 Orders per Customer: {total_orders / total_customers:.2f}")

# Date range
print(f"\n📅 Date Range: {orders['order_date'].min().date()} to {orders['order_date'].max().date()}")
print(f"   Duration: {(orders['order_date'].max() - orders['order_date'].min()).days} days")

print("\n✅ Initial analysis complete!")
print("\nNext steps: Run RFM segmentation")