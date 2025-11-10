"""
Display summary of all analysis results
"""

import pandas as pd
import os

print("=" * 70)
print(" ANALYSIS RESULTS SUMMARY")
print("=" * 70)

# RFM Segmentation Results
print("\n📊 RFM SEGMENTATION:")
if os.path.exists('output/segment_summary.csv'):
    segments = pd.read_csv('output/segment_summary.csv')
    print(segments.to_string())

    # Calculate key metrics
    total_customers = segments['customer_count'].sum()
    total_revenue = segments['total_revenue'].sum()

    print(f"\n   Total Customers Analyzed: {total_customers:,}")
    print(f"   Total Revenue: ${total_revenue:,.2f}")
else:
    print("   ⚠️  Run rfm_analysis.py first")

# Forecast Results
print("\n\n🔮 SALES FORECAST (Next 90 Days):")
if os.path.exists('output/sales_forecast.csv'):
    forecast = pd.read_csv('output/sales_forecast.csv')

    # Convert date column to datetime
    forecast['date'] = pd.to_datetime(forecast['date'])

    # Get future predictions only
    current_date = pd.Timestamp.now()
    future_forecast = forecast[forecast['date'] > current_date]

    if len(future_forecast) > 0:
        predicted_revenue = future_forecast['predicted_revenue'].sum()
        avg_daily = future_forecast['predicted_revenue'].mean()
        lower_bound = future_forecast['lower_bound'].sum()
        upper_bound = future_forecast['upper_bound'].sum()

        print(f"   Predicted Revenue: ${predicted_revenue:,.2f}")
        print(f"   Average Daily: ${avg_daily:,.2f}")
        print(f"   Range: ${lower_bound:,.2f} - ${upper_bound:,.2f}")
        print(f"   Forecast Days: {len(future_forecast)}")
    else:
        # If no future dates, show last 90 days of forecast
        last_90 = forecast.tail(90)
        predicted_revenue = last_90['predicted_revenue'].sum()
        avg_daily = last_90['predicted_revenue'].mean()

        print(f"   Predicted Revenue (Last 90 days): ${predicted_revenue:,.2f}")
        print(f"   Average Daily: ${avg_daily:,.2f}")
        print(f"   Note: Showing historical forecast data")
else:
    print("   ⚠️  Run forecasting.py first")

# RFM Details
print("\n\n👥 CUSTOMER SEGMENT DETAILS:")
if os.path.exists('output/rfm_segmentation.csv'):
    rfm = pd.read_csv('output/rfm_segmentation.csv')

    # Top segments by revenue
    top_segments = rfm.groupby('segment').agg({
        'customer_id': 'count',
        'monetary': 'sum'
    }).sort_values('monetary', ascending=False).head(5)

    top_segments.columns = ['Customers', 'Total Revenue']
    print(top_segments.to_string())

    # High-value opportunity
    high_value = rfm[rfm['segment'].isin(['Champions', 'At Risk', "Can't Lose Them", 'Loyal Customers'])]
    retention_opportunity = high_value['monetary'].sum() * 0.12

    print(f"\n   💰 Retention Revenue Opportunity: ${retention_opportunity:,.2f}")
    print(f"   (12% boost from high-value segments)")
else:
    print("   ⚠️  Run rfm_analysis.py first")

# Files created
print("\n\n📁 OUTPUT FILES:")
if os.path.exists('output'):
    print("\n   CSV Files:")
    csv_files = [f for f in os.listdir('output') if f.endswith('.csv')]
    for file in sorted(csv_files):
        size = os.path.getsize(f'output/{file}') / 1024
        print(f"      • {file} ({size:.1f} KB)")

    if os.path.exists('output/charts'):
        print("\n   📊 Charts:")
        chart_files = [f for f in os.listdir('output/charts') if f.endswith('.png')]
        for file in sorted(chart_files):
            size = os.path.getsize(f'output/charts/{file}') / 1024
            print(f"      • {file} ({size:.1f} KB)")
else:
    print("   ⚠️  No output folder found. Run analyses first.")

# Quick stats from orders
print("\n\n📈 QUICK STATS:")
if os.path.exists('data/orders.csv'):
    orders = pd.read_csv('data/orders.csv')
    orders['order_date'] = pd.to_datetime(orders['order_date'])
    completed_orders = orders[orders['order_status'] == 'Completed']

    print(f"   Total Orders: {len(orders):,}")
    print(f"   Completed Orders: {len(completed_orders):,}")
    print(f"   Total Revenue: ${completed_orders['total_amount'].sum():,.2f}")
    print(f"   Average Order Value: ${completed_orders['total_amount'].mean():.2f}")
    print(f"   Date Range: {orders['order_date'].min().date()} to {orders['order_date'].max().date()}")

    # Unique customers
    unique_customers = completed_orders['customer_id'].nunique()
    print(f"   Unique Customers: {unique_customers:,}")
    print(f"   Orders per Customer: {len(completed_orders) / unique_customers:.2f}")

print("\n" + "=" * 70)
print("\n✅ Results Summary Complete!")
print("\n💡 Next Steps:")
print("   • View charts in output/charts/ folder")
print("   • Run dashboard.py for interactive visualizations")
print("   • Review CSV files for detailed data")
print("=" * 70)