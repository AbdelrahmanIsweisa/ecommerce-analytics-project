"""
RFM Segmentation - Identify high-value customer segments
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import timedelta

print("=" * 60)
print("RFM SEGMENTATION ANALYSIS")
print("=" * 60)

# Load data
orders = pd.read_csv('data/orders.csv')
orders['order_date'] = pd.to_datetime(orders['order_date'])

# Filter completed orders only
orders = orders[orders['order_status'] == 'Completed']

# ====================
# 1. CALCULATE RFM
# ====================
print("\n📊 Calculating RFM metrics...")

# Analysis date (most recent order + 1 day)
analysis_date = orders['order_date'].max() + timedelta(days=1)

# Calculate RFM for each customer
rfm = orders.groupby('customer_id').agg({
    'order_date': lambda x: (analysis_date - x.max()).days,  # Recency
    'order_id': 'count',  # Frequency
    'total_amount': 'sum'  # Monetary
}).reset_index()

rfm.columns = ['customer_id', 'recency', 'frequency', 'monetary']

print(f"✅ Calculated RFM for {len(rfm):,} customers")

# ====================
# 2. CREATE RFM SCORES
# ====================
print("\n🎯 Creating RFM scores...")

# Score on 1-5 scale (5 is best for R, F, M)
# Use rank-based scoring to handle duplicates better
def score_rfm(series, ascending=True):
    """Create 1-5 scores handling duplicates gracefully"""
    try:
        # Try qcut first
        return pd.qcut(series, q=5, labels=False, duplicates='drop') + 1
    except ValueError:
        # If qcut fails due to duplicates, use percentile-based ranking
        return pd.cut(series, bins=5, labels=False, duplicates='drop') + 1

# Recency: Lower is better, so reverse the score (5 = most recent)
rfm['R_score'] = 6 - score_rfm(rfm['recency'], ascending=True)

# Frequency: Higher is better (5 = most frequent)
rfm['F_score'] = score_rfm(rfm['frequency'], ascending=True)

# Monetary: Higher is better (5 = highest spending)
rfm['M_score'] = score_rfm(rfm['monetary'], ascending=True)

# Ensure scores are integers
rfm['R_score'] = rfm['R_score'].astype(int)
rfm['F_score'] = rfm['F_score'].astype(int)
rfm['M_score'] = rfm['M_score'].astype(int)

# Combined RFM score
rfm['RFM_score'] = rfm['R_score'].astype(str) + rfm['F_score'].astype(str) + rfm['M_score'].astype(str)

# ====================
# 3. SEGMENT CUSTOMERS
# ====================
print("\n👥 Segmenting customers...")


def segment_customer(row):
    """Assign customer segment based on RFM scores"""
    r, f, m = row['R_score'], row['F_score'], row['M_score']

    # Champions: Bought recently, buy often, spend most
    if r >= 4 and f >= 4 and m >= 4:
        return 'Champions'

    # Loyal Customers: Buy regularly
    elif r >= 3 and f >= 3 and m >= 3:
        return 'Loyal Customers'

    # Potential Loyalists: Recent customers, good frequency
    elif r >= 4 and f >= 2 and m >= 2:
        return 'Potential Loyalists'

    # At Risk: Used to buy frequently but haven't recently
    elif r <= 2 and f >= 3:
        return 'At Risk'

    # Can't Lose Them: High spenders who haven't bought recently
    elif r <= 2 and m >= 4:
        return "Can't Lose Them"

    # Hibernating: Last purchase long ago, low frequency
    elif r <= 2 and f <= 2:
        return 'Hibernating'

    # New Customers: Recent purchase, low frequency
    elif r >= 4 and f <= 2:
        return 'New Customers'

    else:
        return 'Regular'


rfm['segment'] = rfm.apply(segment_customer, axis=1)

# ====================
# 4. SEGMENT ANALYSIS
# ====================
print("\n" + "=" * 60)
print("SEGMENTATION RESULTS")
print("=" * 60)

segment_summary = rfm.groupby('segment').agg({
    'customer_id': 'count',
    'monetary': ['sum', 'mean'],
    'frequency': 'mean',
    'recency': 'mean'
}).round(2)

segment_summary.columns = ['customer_count', 'total_revenue', 'avg_revenue', 'avg_frequency', 'avg_recency']
segment_summary = segment_summary.sort_values('total_revenue', ascending=False)

print("\n" + segment_summary.to_string())

# ====================
# 5. CALCULATE RETENTION OPPORTUNITY
# ====================
print("\n" + "=" * 60)
print("RETENTION REVENUE OPPORTUNITY")
print("=" * 60)

# Focus on high-value segments
high_value_segments = ['Champions', 'Loyal Customers', 'At Risk', "Can't Lose Them"]
high_value_customers = rfm[rfm['segment'].isin(high_value_segments)]

total_high_value_revenue = high_value_customers['monetary'].sum()
retention_boost = total_high_value_revenue * 0.12  # 12% projected boost

print(f"\n💎 High-Value Segments:")
for seg in high_value_segments:
    count = len(rfm[rfm['segment'] == seg])
    revenue = rfm[rfm['segment'] == seg]['monetary'].sum()
    print(f"   • {seg}: {count:,} customers, ${revenue:,.2f} revenue")

print(f"\n📈 Total High-Value Revenue: ${total_high_value_revenue:,.2f}")
print(f"🎯 Projected 12% Retention Boost: ${retention_boost:,.2f}")
print(f"   (Through targeted re-engagement campaigns)")

# ====================
# 6. SAVE RESULTS
# ====================
rfm.to_csv('output/rfm_segmentation.csv', index=False)
segment_summary.to_csv('output/segment_summary.csv')

print("\n💾 Results saved to output/ folder")
print("\n✅ RFM Analysis Complete!")