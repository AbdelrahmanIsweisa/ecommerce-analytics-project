"""
Create visualizations for dashboard
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("📊 Creating visualizations...")

# Load data
orders = pd.read_csv('data/orders.csv')
orders['order_date'] = pd.to_datetime(orders['order_date'])
orders = orders[orders['order_status'] == 'Completed']

rfm = pd.read_csv('output/rfm_segmentation.csv')

# Create output folder for images
os.makedirs('output/charts', exist_ok=True)

# ====================
# 1. Monthly Revenue Trend
# ====================
print("Creating monthly revenue trend...")

monthly_revenue = orders.groupby(orders['order_date'].dt.to_period('M'))['total_amount'].sum()
monthly_revenue.index = monthly_revenue.index.to_timestamp()

plt.figure(figsize=(14, 6))
plt.plot(monthly_revenue.index, monthly_revenue.values, marker='o', linewidth=2, markersize=6)
plt.title('Monthly Revenue Trend', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('output/charts/monthly_revenue.png', dpi=300, bbox_inches='tight')
plt.close()

# ====================
# 2. Customer Segments Distribution
# ====================
print("Creating segment distribution chart...")

segment_counts = rfm['segment'].value_counts()

plt.figure(figsize=(12, 8))
colors = sns.color_palette('husl', len(segment_counts))
plt.pie(segment_counts.values, labels=segment_counts.index, autopct='%1.1f%%',
        startangle=90, colors=colors, textprops={'fontsize': 11})
plt.title('Customer Segment Distribution', fontsize=18, fontweight='bold', pad=20)
plt.axis('equal')
plt.tight_layout()
plt.savefig('output/charts/segment_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# ====================
# 3. Revenue by Segment
# ====================
print("Creating revenue by segment chart...")

segment_revenue = rfm.groupby('segment')['monetary'].sum().sort_values(ascending=True)

plt.figure(figsize=(12, 6))
colors = plt.cm.viridis(np.linspace(0, 1, len(segment_revenue)))
plt.barh(segment_revenue.index, segment_revenue.values, color=colors)
plt.title('Total Revenue by Customer Segment', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Revenue ($)', fontsize=12)
plt.ylabel('Segment', fontsize=12)
plt.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.savefig('output/charts/revenue_by_segment.png', dpi=300, bbox_inches='tight')
plt.close()

# ====================
# 4. Category Performance (Bonus)
# ====================
print("Creating category performance chart...")

# Load additional data for category analysis
products = pd.read_csv('data/products.csv')
order_items = pd.read_csv('data/order_items.csv')

# Merge and calculate category revenue
category_data = order_items.merge(products, on='product_id')
category_revenue = category_data.groupby('category').agg({
    'quantity': 'sum',
    'unit_price': lambda x: (x * category_data.loc[x.index, 'quantity']).sum()
}).reset_index()
category_revenue.columns = ['category', 'units_sold', 'revenue']
category_revenue = category_revenue.sort_values('revenue', ascending=False)

plt.figure(figsize=(12, 6))
bars = plt.bar(category_revenue['category'], category_revenue['revenue'],
               color=sns.color_palette('coolwarm', len(category_revenue)))
plt.title('Revenue by Product Category', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('output/charts/category_performance.png', dpi=300, bbox_inches='tight')
plt.close()

# ====================
# 5. RFM Score Distribution (Heatmap)
# ====================
print("Creating RFM score heatmap...")

# Create pivot table for heatmap
rfm_pivot = rfm.groupby(['R_score', 'F_score']).size().reset_index(name='count')
rfm_matrix = rfm_pivot.pivot(index='F_score', columns='R_score', values='count').fillna(0)

plt.figure(figsize=(10, 8))
sns.heatmap(rfm_matrix, annot=True, fmt='.0f', cmap='YlOrRd',
            cbar_kws={'label': 'Number of Customers'})
plt.title('RFM Score Distribution (Recency vs Frequency)', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Recency Score', fontsize=12)
plt.ylabel('Frequency Score', fontsize=12)
plt.tight_layout()
plt.savefig('output/charts/rfm_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()

print("\n✅ All charts saved to output/charts/")
print("\nCharts created:")
print("   • monthly_revenue.png")
print("   • segment_distribution.png")
print("   • revenue_by_segment.png")
print("   • category_performance.png")
print("   • rfm_heatmap.png")