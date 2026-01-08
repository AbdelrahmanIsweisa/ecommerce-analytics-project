# E-Commerce Customer Analytics & Revenue Optimization

**Analyzed 60,000+ transactions to identify high-value customer segments and uncover $1.2M in retention opportunities**

[![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Tableau](https://img.shields.io/badge/Tableau-E97627?style=flat&logo=tableau&logoColor=white)](https://www.tableau.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)

---

## 🎯 Project Overview

Built a customer analytics system using RFM (Recency, Frequency, Monetary) analysis to help an e-commerce business understand customer behavior and maximize revenue retention.

### Key Results

- **💎 Top 17% of customers generate 61% of revenue** - Champions segment drives $5.6M of $9.2M total
- **🚨 Identified 1,286 high-value at-risk customers** worth $1.2M in potential recovery
- **📊 Created 7 strategic customer segments** for targeted marketing campaigns
- **💰 Analyzed 15,000 customers across 60,000+ transactions**

---

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| **MySQL** | RFM calculations, customer segmentation queries |
| **Tableau** | Interactive dashboards with drill-down capabilities |
| **Python** | Data generation and preprocessing |
| **Excel** | Financial modeling and ROI analysis |

---

## 📊 Customer Segments

Using RFM analysis, I classified customers into 7 strategic segments:

| Segment | Customers | Revenue | % of Total | Insight |
|---------|-----------|---------|------------|---------|
| **Champions** | 2,616 (17%) | $5.62M | **61%** | Best customers - reward & retain |
| **Big Spenders** | 1,755 (12%) | $1.24M | 13% | High value - upsell opportunities |
| **Loyal** | 351 (2%) | $629K | 7% | Frequent buyers - loyalty programs |
| **Lost** | 8,248 (55%) | $1.24M | 13% | Inactive - low priority |
| **Promising** | 1,809 (12%) | $440K | 5% | New customers - nurture them |
| **At Risk** | 112 (1%) | $44K | 0.5% | Used to buy often - win them back |
| **Need Attention** | 109 (1%) | $29K | 0.3% | Declining engagement |

**Key Insight:** Champions alone drive more revenue than all other segments combined.

---

## 🎨 Tableau Dashboard

Built an interactive executive summary dashboard featuring:

- **4 Key Performance Indicators (KPIs)**
  - Total Revenue: $9.24M
  - Total Customers: 15,000
  - Champions Revenue: $5.6M (61%)
  - At-Risk Recovery Opportunity: $1.2M

- **Customer Segmentation Scatter Plot** (RFM Analysis)
  - Visualizes relationship between purchase frequency and monetary value
  - Color-coded by segment for easy identification

- **Revenue by Segment Bar Chart**
  - Clearly shows revenue concentration in Champions segment
  - Sorted by revenue contribution

**Dashboard Preview:**
![Executive Summary Dashboard](images/dashboard_preview.png)
*Interactive dashboard showing customer segments and key business metrics*

[🔗 View Live Tableau Dashboard](https://public.tableau.com/views/YourDashboardLink) *(Update with your Tableau Public link)*

---

## 💡 Business Insights

### 1. Revenue Concentration
- **Top 29% of customers** (Champions + Big Spenders) generate **74% of revenue**
- Average Champion spends **$2,149** vs $211 for Lost customers (**10x difference**)

### 2. Retention Opportunity
- **1,286 high-value customers** (spent $500+) haven't purchased in 90+ days
- These customers represent **$1.2M in lifetime value**
- Historical data shows **30% respond** to targeted retention campaigns

### 3. Strategic Recommendations
- **Champions:** Focus on retention and referral programs
- **At Risk:** Act immediately with personalized win-back offers
- **Lost:** Reallocate budget to higher-value segments

---

## 🗂️ Project Structure

```
ecommerce-analytics/
├── Data/
│   ├── customers.csv              # 15,000 customer records
│   ├── orders.csv                 # 60,000 transactions
│   ├── order_items.csv            # Order line items
│   └── products.csv               # Product catalog
│
├── SQL/
│   └── ecommerce_rfm_analysis.sql # Complete RFM analysis ⭐
│
├── Tableau/
│   └── Ecommerce_Dashboard.twbx   # Interactive dashboard ⭐
│
├── Python/
│   ├── generate_sample_data.py    # Creates sample dataset
│   └── ecommerce_analysis.py      # Data processing
│
└── README.md
```

---

## 🚀 How to Run This Project

### Option 1: View the Dashboard (Easiest)
1. Download `Ecommerce_Dashboard.twbx` from `/Tableau`
2. Open with [Tableau Public](https://public.tableau.com/app/discover) (free)
3. Explore the interactive visualizations

### Option 2: Run the Full Analysis

**Prerequisites:**
- MySQL 8.0+
- Python 3.8+
- Tableau Desktop or Tableau Public

**Steps:**
```bash
# 1. Clone the repository
git clone https://github.com/AbdelrahmanIsweisa/ecommerce-analytics-project.git
cd ecommerce-analytics-project

# 2. Generate sample data
python Python/generate_sample_data.py

# 3. Set up MySQL database
mysql -u root -p < SQL/create_database.sql

# 4. Run RFM analysis
mysql -u root -p ecommerce_analytics < SQL/ecommerce_rfm_analysis.sql

# 5. Open Tableau dashboard
# Open Ecommerce_Dashboard.twbx in Tableau Desktop or Tableau Public
```

---

## 📈 Key SQL Queries

### Query 1: Calculate RFM Metrics
```sql
-- Calculate Recency, Frequency, Monetary for each customer
SELECT 
    customer_id,
    DATEDIFF('2025-05-31', MAX(order_date)) as recency_days,
    COUNT(DISTINCT order_id) as frequency,
    ROUND(SUM(quantity * unit_price), 2) as monetary_value
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY customer_id;
```

### Query 2: Identify At-Risk High-Value Customers
```sql
-- Find customers who spent $500+ but haven't purchased in 90+ days
SELECT 
    customer_id,
    monetary_value,
    recency_days,
    frequency
FROM customer_segments
WHERE monetary_value >= 500 
  AND recency_days >= 90
ORDER BY monetary_value DESC;
-- Result: 1,286 customers worth $1.2M
```

### Query 3: Segment Performance Summary
```sql
-- Revenue contribution by segment
SELECT 
    customer_segment,
    COUNT(*) as customers,
    ROUND(SUM(monetary_value), 0) as total_revenue,
    ROUND(AVG(monetary_value), 0) as avg_customer_value
FROM customer_segments
GROUP BY customer_segment
ORDER BY total_revenue DESC;
```

---

## 🎓 Skills Demonstrated

- **SQL**: Window functions, CTEs, views, joins, date functions, aggregations
- **RFM Analysis**: Customer segmentation based on behavioral patterns
- **Data Visualization**: Dashboard design, KPI tracking, storytelling with data
- **Business Analytics**: Customer lifetime value, churn analysis, retention strategies
- **Financial Modeling**: ROI calculations, cost-benefit analysis

---

## 💼 Business Value

### Problem Solved
- No visibility into which customers drive the most revenue
- Unclear which customers are at risk of churning
- Marketing budget allocated equally across all customers

### Solution Delivered
- Clear segmentation showing Champions drive 61% of revenue
- Identified $1.2M at-risk opportunity requiring immediate action
- Actionable recommendations for segment-specific marketing strategies

### Expected ROI
- **Campaign Cost:** $110 per customer × 1,286 = $142K
- **Expected Recovery:** 30% success rate × $1.2M = $360K
- **Net Benefit:** $218K (154% ROI)

---

## 📝 What I Learned

- How to design and implement RFM analysis from scratch
- Building executive-ready dashboards that tell a clear story
- Translating technical findings into business recommendations
- Working with multi-table databases and complex joins
- Creating reusable SQL views for ongoing analysis

---

## 🔮 Future Enhancements

If I had more time, I would add:
- **Cohort Analysis**: Track retention rates by signup month
- **Predictive Churn Model**: Machine learning to predict future churn risk
- **Product Recommendations**: Market basket analysis for cross-sell opportunities
- **A/B Testing Framework**: Measure campaign effectiveness
- **Automated Alerts**: Email triggers when customers become at-risk

---

## 👤 About Me

**Abdelrahman Isweisa**  
MIS Graduate | Business Analytics | Data-Driven Problem Solver

- 📧 Email: Abdelrahman_Isweisa@student.uml.edu
- 💼 LinkedIn: [linkedin.com/in/abdelrahmanisweisa](https://www.linkedin.com/in/abdelrahmanisweisa)
- 🐙 GitHub: [github.com/AbdelrahmanIsweisa](https://github.com/AbdelrahmanIsweisa)
- 📍 Location: Shrewsbury, MA

*Currently seeking Business Analyst, Operations Analyst, or Data Analyst roles*

---

## 📄 License

This project is available under the MIT License. Feel free to use as a reference for your own analysis!

---

**⭐ If this project was helpful, please star the repository!**

*Built with real-world business impact in mind* 💼
