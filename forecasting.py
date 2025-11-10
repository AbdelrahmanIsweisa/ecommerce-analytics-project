"""
Sales forecasting using Prophet
"""

import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

print("=" * 60)
print("SALES FORECASTING - PROPHET MODEL")
print("=" * 60)

# Load data
orders = pd.read_csv('data/orders.csv')
orders['order_date'] = pd.to_datetime(orders['order_date'])
orders = orders[orders['order_status'] == 'Completed']

# ====================
# 1. PREPARE DATA FOR PROPHET
# ====================
print("\n📊 Preparing time series data...")

# Aggregate daily sales
prophet_data = orders.groupby('order_date')['total_amount'].sum().reset_index()
prophet_data.columns = ['ds', 'y']  # Prophet requires these column names

print(f"✅ Data prepared: {len(prophet_data)} days of sales data")
print(f"   Date range: {prophet_data['ds'].min().date()} to {prophet_data['ds'].max().date()}")

# ====================
# 2. CREATE AND TRAIN MODEL
# ====================
print("\n🤖 Training Prophet model...")

model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=True,
    daily_seasonality=False,
    seasonality_mode='multiplicative',
    changepoint_prior_scale=0.05
)

model.fit(prophet_data)
print("✅ Model training complete!")

# ====================
# 3. MAKE PREDICTIONS
# ====================
print("\n🔮 Generating forecast for next 90 days...")

# Create future dataframe (90 days ahead)
future = model.make_future_dataframe(periods=90)
forecast = model.predict(future)

# ====================
# 4. CALCULATE METRICS
# ====================
next_quarter = forecast[forecast['ds'] > orders['order_date'].max()]
predicted_revenue = next_quarter['yhat'].sum()
predicted_lower = next_quarter['yhat_lower'].sum()
predicted_upper = next_quarter['yhat_upper'].sum()

print("\n" + "=" * 60)
print("FORECAST RESULTS - NEXT QUARTER (90 DAYS)")
print("=" * 60)
print(f"\n📈 Predicted Revenue: ${predicted_revenue:,.2f}")
print(f"   Lower Bound (80% confidence): ${predicted_lower:,.2f}")
print(f"   Upper Bound (80% confidence): ${predicted_upper:,.2f}")

# Calculate average daily revenue
avg_daily_forecast = next_quarter['yhat'].mean()
print(f"\n📊 Average Daily Revenue (forecast): ${avg_daily_forecast:,.2f}")

# Historical comparison
historical_avg = prophet_data['y'].mean()
growth_rate = ((avg_daily_forecast - historical_avg) / historical_avg) * 100
print(f"   Historical Average: ${historical_avg:,.2f}")
print(f"   Projected Growth: {growth_rate:+.1f}%")

# ====================
# 5. CREATE VISUALIZATIONS
# ====================
print("\n📊 Creating forecast visualizations...")

# Main forecast plot
fig1 = model.plot(forecast, figsize=(14, 6))
plt.title('Sales Forecast - Next 90 Days', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Daily Revenue ($)', fontsize=12)
plt.tight_layout()
plt.savefig('output/charts/sales_forecast.png', dpi=300, bbox_inches='tight')
plt.close()

# Components plot (trend, seasonality)
fig2 = model.plot_components(forecast, figsize=(14, 10))
plt.tight_layout()
plt.savefig('output/charts/forecast_components.png', dpi=300, bbox_inches='tight')
plt.close()

# ====================
# 6. SAVE FORECAST DATA
# ====================
forecast_export = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].copy()
forecast_export.columns = ['date', 'predicted_revenue', 'lower_bound', 'upper_bound']
forecast_export.to_csv('output/sales_forecast.csv', index=False)

print("\n💾 Forecast saved to output/sales_forecast.csv")
print("📊 Charts saved to output/charts/")
print("\n✅ Forecasting Complete!")