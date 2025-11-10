"""
Interactive Executive Dashboard using Plotly Dash
Real-time data visualization for e-commerce analytics
"""

import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

print("=" * 70)
print("🚀 LOADING DASHBOARD DATA...")
print("=" * 70)

# Load data
orders = pd.read_csv('data/orders.csv')
orders['order_date'] = pd.to_datetime(orders['order_date'])
orders = orders[orders['order_status'] == 'Completed']

rfm = pd.read_csv('output/rfm_segmentation.csv')
products = pd.read_csv('data/products.csv')
order_items = pd.read_csv('data/order_items.csv')

# Calculate KPIs
total_revenue = orders['total_amount'].sum()
total_orders = len(orders)
avg_order_value = orders['total_amount'].mean()
total_customers = orders['customer_id'].nunique()

# Calculate retention opportunity
high_value_segments = ['Champions', 'At Risk', "Can't Lose Them", 'Loyal Customers']
high_value_customers = rfm[rfm['segment'].isin(high_value_segments)]
retention_opportunity = high_value_customers['monetary'].sum() * 0.12

print(f"✅ Data loaded successfully!")
print(f"   • {len(orders):,} orders")
print(f"   • {total_customers:,} customers")
print(f"   • ${total_revenue:,.2f} total revenue")

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "E-Commerce Analytics Dashboard"

# Define layout
app.layout = html.Div([
    # Header
    html.Div([
        html.H1("📊 E-Commerce Analytics Dashboard",
                style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': 10}),
        html.P("Real-time Customer Insights & Sales Performance",
               style={'textAlign': 'center', 'color': '#7f8c8d', 'fontSize': 16})
    ], style={'padding': '20px'}),

    # KPI Cards
    html.Div([
        html.Div([
            html.Div([
                html.P("💰 Total Revenue", style={'color': '#7f8c8d', 'fontSize': 14, 'margin': 0}),
                html.H2(f"${total_revenue:,.0f}", style={'color': '#27ae60', 'margin': '10px 0'})
            ], style={'padding': '20px', 'backgroundColor': '#ecf0f1',
                      'borderRadius': '10px', 'textAlign': 'center', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'})
        ], style={'flex': 1, 'margin': '10px'}),

        html.Div([
            html.Div([
                html.P("📦 Total Orders", style={'color': '#7f8c8d', 'fontSize': 14, 'margin': 0}),
                html.H2(f"{total_orders:,}", style={'color': '#3498db', 'margin': '10px 0'})
            ], style={'padding': '20px', 'backgroundColor': '#ecf0f1',
                      'borderRadius': '10px', 'textAlign': 'center', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'})
        ], style={'flex': 1, 'margin': '10px'}),

        html.Div([
            html.Div([
                html.P("💵 Avg Order Value", style={'color': '#7f8c8d', 'fontSize': 14, 'margin': 0}),
                html.H2(f"${avg_order_value:.2f}", style={'color': '#e74c3c', 'margin': '10px 0'})
            ], style={'padding': '20px', 'backgroundColor': '#ecf0f1',
                      'borderRadius': '10px', 'textAlign': 'center', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'})
        ], style={'flex': 1, 'margin': '10px'}),

        html.Div([
            html.Div([
                html.P("👥 Total Customers", style={'color': '#7f8c8d', 'fontSize': 14, 'margin': 0}),
                html.H2(f"{total_customers:,}", style={'color': '#9b59b6', 'margin': '10px 0'})
            ], style={'padding': '20px', 'backgroundColor': '#ecf0f1',
                      'borderRadius': '10px', 'textAlign': 'center', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'})
        ], style={'flex': 1, 'margin': '10px'}),
    ], style={'display': 'flex', 'justifyContent': 'space-around', 'marginBottom': 20, 'padding': '0 20px'}),

    # Retention Opportunity Banner
    html.Div([
        html.Div([
            html.H3(f"🎯 Retention Revenue Opportunity: ${retention_opportunity:,.0f}",
                    style={'color': '#fff', 'margin': 0}),
            html.P("12% projected boost from high-value customer segments",
                   style={'color': '#fff', 'fontSize': 14, 'margin': '5px 0 0 0'})
        ], style={'padding': '15px', 'backgroundColor': '#e67e22', 'borderRadius': '10px',
                  'textAlign': 'center', 'boxShadow': '0 2px 4px rgba(0,0,0,0.2)'})
    ], style={'padding': '0 20px', 'marginBottom': 20}),

    # Charts Row 1
    html.Div([
        html.Div([
            dcc.Graph(id='revenue-trend')
        ], style={'width': '65%', 'display': 'inline-block', 'padding': '0 10px'}),

        html.Div([
            dcc.Graph(id='segment-pie')
        ], style={'width': '35%', 'display': 'inline-block', 'padding': '0 10px'})
    ], style={'marginBottom': 20}),

    # Charts Row 2
    html.Div([
        html.Div([
            dcc.Graph(id='segment-revenue-bar')
        ], style={'width': '50%', 'display': 'inline-block', 'padding': '0 10px'}),

        html.Div([
            dcc.Graph(id='category-performance')
        ], style={'width': '50%', 'display': 'inline-block', 'padding': '0 10px'})
    ], style={'marginBottom': 20}),

    # Footer
    html.Div([
        html.P("📊 E-Commerce Analytics Project | Built with Python, Dash, and Plotly",
               style={'textAlign': 'center', 'color': '#95a5a6', 'fontSize': 12})
    ], style={'padding': '20px'})

], style={'fontFamily': 'Arial, sans-serif', 'backgroundColor': '#f5f6fa'})


# Callbacks for interactive charts
@app.callback(
    Output('revenue-trend', 'figure'),
    Input('revenue-trend', 'id')
)
def update_revenue_trend(_):
    """Monthly revenue trend with moving average"""
    monthly_data = orders.groupby(orders['order_date'].dt.to_period('M'))['total_amount'].sum().reset_index()
    monthly_data['order_date'] = monthly_data['order_date'].astype(str)

    fig = go.Figure()

    # Add revenue line
    fig.add_trace(go.Scatter(
        x=monthly_data['order_date'],
        y=monthly_data['total_amount'],
        mode='lines+markers',
        name='Revenue',
        line=dict(color='#3498db', width=3),
        marker=dict(size=8),
        hovertemplate='<b>%{x}</b><br>Revenue: $%{y:,.0f}<extra></extra>'
    ))

    fig.update_layout(
        title='Monthly Revenue Trend',
        xaxis_title='Month',
        yaxis_title='Revenue ($)',
        hovermode='x unified',
        template='plotly_white',
        height=400
    )

    return fig


@app.callback(
    Output('segment-pie', 'figure'),
    Input('segment-pie', 'id')
)
def update_segment_pie(_):
    """Customer segment distribution"""
    segment_counts = rfm['segment'].value_counts().reset_index()
    segment_counts.columns = ['segment', 'count']

    fig = px.pie(
        segment_counts,
        values='count',
        names='segment',
        title='Customer Segment Distribution',
        color_discrete_sequence=px.colors.qualitative.Set3,
        hole=0.4  # Donut chart
    )

    fig.update_traces(
        textposition='inside',
        textinfo='percent+label',
        hovertemplate='<b>%{label}</b><br>Customers: %{value:,}<br>Percentage: %{percent}<extra></extra>'
    )

    fig.update_layout(height=400)

    return fig


@app.callback(
    Output('segment-revenue-bar', 'figure'),
    Input('segment-revenue-bar', 'id')
)
def update_segment_revenue(_):
    """Revenue by customer segment"""
    segment_revenue = rfm.groupby('segment')['monetary'].sum().reset_index()
    segment_revenue = segment_revenue.sort_values('monetary', ascending=True)

    fig = go.Figure(go.Bar(
        x=segment_revenue['monetary'],
        y=segment_revenue['segment'],
        orientation='h',
        marker=dict(
            color=segment_revenue['monetary'],
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title="Revenue ($)")
        ),
        hovertemplate='<b>%{y}</b><br>Revenue: $%{x:,.0f}<extra></extra>'
    ))

    fig.update_layout(
        title='Revenue by Customer Segment',
        xaxis_title='Total Revenue ($)',
        yaxis_title='',
        template='plotly_white',
        height=400
    )

    return fig


@app.callback(
    Output('category-performance', 'figure'),
    Input('category-performance', 'id')
)
def update_category_performance(_):
    """Revenue by product category"""
    category_data = order_items.merge(products, on='product_id')
    category_revenue = category_data.groupby('category').agg({
        'quantity': 'sum',
        'unit_price': lambda x: (x * category_data.loc[x.index, 'quantity']).sum()
    }).reset_index()
    category_revenue.columns = ['category', 'units_sold', 'revenue']
    category_revenue = category_revenue.sort_values('revenue', ascending=False)

    fig = go.Figure(go.Bar(
        x=category_revenue['category'],
        y=category_revenue['revenue'],
        marker=dict(
            color=category_revenue['revenue'],
            colorscale='Blues',
            showscale=False
        ),
        hovertemplate='<b>%{x}</b><br>Revenue: $%{y:,.0f}<extra></extra>'
    ))

    fig.update_layout(
        title='Revenue by Product Category',
        xaxis_title='',
        yaxis_title='Revenue ($)',
        xaxis_tickangle=-45,
        template='plotly_white',
        height=400
    )

    return fig


# Run server
if __name__ == '__main__':
    print("\n" + "=" * 70)
    print("🚀 STARTING DASHBOARD SERVER")
    print("=" * 70)
    print("\n📊 Dashboard running at: http://127.0.0.1:8050/")
    print("\n💡 Instructions:")
    print("   1. Click the link above (or copy to browser)")
    print("   2. Interact with the charts (hover, zoom, pan)")
    print("   3. Press Ctrl+C in terminal to stop")
    print("\n" + "=" * 70 + "\n")

    app.run(debug=True, use_reloader=False)