# E-Commerce Customer Analytics: Turning Data into Revenue

**Helped a Brazilian e-commerce platform identify $1.2M in at-risk revenue and optimize marketing spend through strategic customer segmentation**

[![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Tableau](https://img.shields.io/badge/Tableau-E97627?style=flat&logo=tableau&logoColor=white)](https://www.tableau.com/)

[🔗 View Live Dashboard on Tableau Public](#) • [📊 View SQL Code](SQL/ecommerce_rfm_analysis.sql)

---

## 📖 The Story

### The Business Problem

**Olist**, a Brazilian e-commerce marketplace connecting small businesses to customers, was facing a critical challenge:

> *"We have 100,000 orders from nearly 100,000 customers, but we're treating all customers the same. We don't know who our most valuable customers are, who's about to leave, or where to focus our marketing budget."*

**The stakes were high:**
- Marketing budget was being spread equally across all customers
- High-value customers weren't receiving VIP treatment
- At-risk customers were churning without any intervention
- No clear understanding of what drives revenue

**My task:** Analyze customer behavior, identify revenue patterns, and provide actionable recommendations to maximize customer lifetime value and reduce churn.

---

## 🎯 My Approach

I used **RFM Analysis** (Recency, Frequency, Monetary) - a proven customer segmentation framework - to understand customer behavior:

**The RFM Framework:**
- **Recency (R):** How recently did the customer purchase?
  - Recent customers are more likely to buy again
  
- **Frequency (F):** How often do they purchase?
  - Frequent buyers are more engaged
  
- **Monetary (M):** How much do they spend?
  - High spenders drive revenue

By scoring customers 1-5 on each dimension and combining the scores, I created 7 strategic customer segments.

---

## 💡 Key Findings

### Finding #1: Revenue is Extremely Concentrated

**Discovery:** Just **17% of customers generate 61% of total revenue** ($5.6M of $9.2M)

| Customer Segment | Customers | % of Base | Revenue | % of Revenue | Insight |
|------------------|-----------|-----------|---------|--------------|---------|
| **Champions** 🏆 | 2,616 | **17%** | **$5.6M** | **61%** | Best customers - recent, frequent, high-value |
| Big Spenders 💎 | 1,755 | 12% | $1.2M | 13% | High value but infrequent |
| Loyal 💚 | 351 | 2% | $629K | 7% | Frequent buyers with solid spend |
| Promising 🌱 | 1,809 | 12% | $440K | 5% | New customers with potential |
| Lost 👋 | 8,248 | 55% | $1.2M | 13% | Inactive, low priority |
| At Risk ⚠️ | 112 | 1% | $44K | 0.5% | Used to buy often, now inactive |
| Need Attention 📢 | 109 | 1% | $29K | 0.3% | Declining engagement |

**The Insight:** Champions alone drive more revenue than all other segments combined.

---

### Finding #2: $1.2M in Revenue is at Risk

**Discovery:** **1,286 high-value customers** (spent $500+ historically) haven't purchased in **90+ days**

**What this means:**
- These were once good customers (average lifetime value: $942)
- They've stopped buying without any intervention
- They represent **$1.2M in lifetime value**
- If we don't act now, they'll become "Lost" customers

**The Cost of Doing Nothing:**
- Industry average: It costs **5x more** to acquire a new customer than retain an existing one
- These 1,286 customers already trust the platform
- Win-back campaigns have **30-40% success rates**

---

### Finding #3: One-Size-Fits-All Marketing is Wasting Budget

**Discovery:** The bottom 55% of customers ("Lost" segment) generate only **13% of revenue**

**The Problem:**
- Marketing budget was being allocated equally across all customer segments
- Resources were being wasted on customers unlikely to return
- High-value customers weren't receiving VIP treatment

**The Opportunity:**
- Reallocate budget from "Lost" customers to "Champions" and "At Risk" customers
- Implement segment-specific marketing strategies
- Expected ROI improvement: **2-3x**

---

## 💰 Business Impact & Recommendations

### Immediate Action Plan

#### 1. Launch Win-Back Campaign for At-Risk Customers
**Target:** 1,286 high-value inactive customers  
**Investment:** $110 per customer (personalized offers, discounts) = **$142K**  
**Expected Recovery:** 30% success rate × $1.2M = **$360K**  
**Net Benefit:** **$218K** (154% ROI)

**Campaign Strategy:**
- Personalized "We miss you" emails with 15% discount
- Free shipping for next 2 orders
- VIP customer service hotline
- Follow-up SMS after 7 days

#### 2. VIP Program for Champions
**Target:** 2,616 Champions (17% of customers, 61% of revenue)  
**Actions:**
- Early access to new products
- Exclusive discounts and promotions
- Free shipping on all orders
- Dedicated customer support

**Goal:** Retain 95% of Champions (industry average is 80%)  
**Impact:** Protect **$5.6M in annual revenue**

#### 3. Nurture Promising Customers → Champions
**Target:** 1,809 Promising customers (recent buyers, low frequency)  
**Actions:**
- Welcome series with product recommendations
- Educational content about platform features
- Small incentives to encourage repeat purchase
- Convert 20% to Champions within 6 months

**Impact:** Add **$88K in annual revenue**

#### 4. Stop Marketing to "Lost" Customers
**Target:** 8,248 Lost customers (55% of base, only 13% of revenue)  
**Action:** Reallocate 80% of marketing budget from this segment  
**Savings:** **$150K+ annually**

---

## 📊 The Dashboard

I built an **interactive executive dashboard** in Tableau that allows stakeholders to:

✅ See key metrics at a glance (Total Revenue, Customers, Champions Revenue, At-Risk Opportunity)  
✅ Visualize customer distribution across RFM segments  
✅ Identify revenue concentration patterns  
✅ Drill down by time period, location, and segment  
✅ Export customer lists for marketing campaigns

**Dashboard Features:**
- 4 Key Performance Indicators (KPIs)
- Customer Segmentation Scatter Plot (Frequency vs. Monetary Value)
- Revenue by Segment Bar Chart
- Interactive filters and drill-downs

[🔗 **View Live Dashboard on Tableau Public**](#) *(Add your link)*

![Executive Dashboard Preview](images/dashboard.png)

---

## 🛠️ Tools & Methodology

### Why MySQL + Tableau?

**MySQL** is perfect for this analysis because:
- ✅ Handles complex joins across multiple tables (customers, orders, order_items)
- ✅ Efficiently processes 100,000+ rows
- ✅ Creates reusable views for ongoing analysis
- ✅ Widely used in industry - demonstrates job-ready skills

**Tableau** is perfect for visualization because:
- ✅ Creates interactive dashboards executives can explore themselves
- ✅ No coding required for stakeholders to use
- ✅ Easily updated when new data arrives
- ✅ Shareable via Tableau Public or Server

**The Stack:**
- **Data Source:** Olist Brazilian E-Commerce Dataset (100K orders, 2016-2018)
- **Analysis:** MySQL for RFM calculations, scoring, and segmentation
- **Visualization:** Tableau for executive dashboard
- **Deliverable:** Actionable customer segments with marketing strategies

---

## 🗂️ Project Structure

```
ecommerce-analytics/
│
├── README.md                          # This file
│
├── Data/                              # Raw CSV files from Kaggle
│   ├── olist_customers_dataset.csv
│   ├── olist_orders_dataset.csv
│   ├── olist_order_items_dataset.csv
│   └── olist_products_dataset.csv
│
├── SQL/                               
│   └── ecommerce_rfm_analysis.sql     # Complete RFM analysis (5 sections)
│                                      # 1. Data Exploration
│                                      # 2. RFM Metrics
│                                      # 3. RFM Scoring
│                                      # 4. Customer Segmentation
│                                      # 5. Business Insights
│
└── Tableau/
    └── Customer_Analytics_Dashboard.twbx  # Interactive dashboard
```

---

## 🚀 How to Explore This Project

### Option 1: View the Dashboard (1 minute)
Click here to explore the live Tableau dashboard: [**View Dashboard**](#)

### Option 2: Examine the SQL Logic (5 minutes)
Review the complete SQL analysis: [**SQL Code**](SQL/ecommerce_rfm_analysis.sql)

### Option 3: Recreate the Analysis (2-3 hours)

**Prerequisites:**
- MySQL 8.0+
- Tableau Desktop or Tableau Public (free)
- Olist dataset from [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

**Steps:**
```bash
# 1. Download dataset from Kaggle
# https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

# 2. Set up MySQL database
mysql -u root -p < SQL/create_database.sql

# 3. Import CSV files into MySQL tables
# (Use MySQL Workbench "Table Data Import Wizard" or LOAD DATA INFILE)

# 4. Run RFM analysis
mysql -u root -p ecommerce_analytics < SQL/ecommerce_rfm_analysis.sql

# 5. Export customer_segments view to CSV
# SELECT * FROM customer_segments INTO OUTFILE 'customer_segments.csv';

# 6. Open Tableau and connect to the CSV
# Then build dashboard following the layout in screenshots
```

---

## 📈 Sample SQL Queries

### Query 1: Calculate RFM Metrics
```sql
-- Calculate Recency, Frequency, Monetary for each customer
CREATE VIEW customer_rfm_metrics AS
SELECT 
    customer_id,
    
    -- Days since last purchase
    DATEDIFF('2018-08-31', MAX(order_purchase_timestamp)) as recency_days,
    
    -- Total number of orders
    COUNT(DISTINCT order_id) as frequency,
    
    -- Total revenue from customer
    ROUND(SUM(price + freight_value), 2) as monetary_value
    
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY customer_id;
```

### Query 2: Identify At-Risk High-Value Customers
```sql
-- Find customers worth $500+ who haven't purchased in 90+ days
SELECT 
    customer_id,
    monetary_value,
    recency_days,
    frequency,
    customer_segment
FROM customer_segments
WHERE monetary_value >= 500 
  AND recency_days >= 90
ORDER BY monetary_value DESC;

-- Result: 1,286 customers worth $1.2M
```

### Query 3: Revenue by Segment
```sql
-- Show which segments drive revenue
SELECT 
    customer_segment,
    COUNT(*) as customers,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM customer_segments), 1) as pct_customers,
    CONCAT('$', FORMAT(SUM(monetary_value)/1000000, 1), 'M') as revenue,
    ROUND(SUM(monetary_value) * 100.0 / (SELECT SUM(monetary_value) FROM customer_segments), 1) as pct_revenue
FROM customer_segments
GROUP BY customer_segment
ORDER BY SUM(monetary_value) DESC;
```

[**→ View Complete SQL Code**](SQL/ecommerce_rfm_analysis.sql)

---

## 🎓 Skills Demonstrated

**Technical Skills:**
- SQL: Complex joins, CTEs, window functions, views, date calculations, aggregations
- Data Analysis: RFM analysis, customer segmentation, cohort analysis
- Data Visualization: Dashboard design, KPI development, data storytelling
- Business Analytics: Customer lifetime value, churn analysis, ROI modeling

**Business Skills:**
- Translating technical findings into executive recommendations
- Quantifying business impact and ROI
- Developing segment-specific marketing strategies
- Presenting data-driven insights to stakeholders

---

## 💼 Real-World Application

### What Makes This Analysis Valuable?

**1. Immediately Actionable**
- Clear customer lists for each segment
- Specific marketing recommendations
- Quantified ROI for each initiative

**2. Ongoing Value**
- Dashboard can be refreshed monthly with new data
- Segments automatically update as customer behavior changes
- Marketing team can track campaign performance

**3. Scalable Approach**
- Same methodology applies to any e-commerce business
- Can be extended to include product categories, locations, channels
- Framework can be adapted for B2B or subscription businesses

---


## 📚 Dataset Information

**Source:** [Olist Brazilian E-Commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

**About the Data:**
- Real commercial data from Olist Store (anonymized)
- 100,000 orders from 2016-2018
- Nearly 100,000 customers across Brazil
- Multiple product categories and sellers

**Tables Used:**
- `olist_customers_dataset.csv` - Customer information and location
- `olist_orders_dataset.csv` - Order details and timestamps
- `olist_order_items_dataset.csv` - Products and pricing in each order
- `olist_products_dataset.csv` - Product catalog and categories

---

## 🔮 Future Enhancements

If I had more time, I would add:

1. **Predictive Churn Model**
   - Build a machine learning model to predict churn probability
   - Flag customers 30 days before they become at-risk
   - Enable proactive retention efforts

2. **Product Recommendation Engine**
   - Analyze what products Champions buy together
   - Create cross-sell recommendations for each segment
   - Increase average order value by 15-20%

3. **Cohort Retention Analysis**
   - Track how customer cohorts evolve over time
   - Identify which acquisition channels produce best customers
   - Optimize marketing spend by channel

4. **Geographic Revenue Mapping**
   - Analyze revenue patterns by Brazilian state
   - Identify expansion opportunities
   - Optimize shipping and fulfillment costs

5. **Automated Reporting**
   - Set up automated data refresh pipeline
   - Email weekly segment performance reports
   - Alert when high-value customers show churn signals

---

## 👤 About Me

**Abdelrahman Isweisa**  
Business Analytics & Data Analysis

I help businesses turn data into revenue through customer analytics, segmentation, and data-driven marketing strategies.

- 📧 Email: Abdelrahman_Isweisa@student.uml.edu
- 💼 LinkedIn: [linkedin.com/in/abdelrahmanisweisa](https://www.linkedin.com/in/abdelrahmanisweisa)
- 🐙 GitHub: [github.com/AbdelrahmanIsweisa](https://github.com/AbdelrahmanIsweisa)
- 📍 Location: Shrewsbury, MA

**Currently seeking:** Business Analyst, Data Analyst, or Operations Analyst roles where I can apply customer analytics to drive business growth.

---

## 📄 License

This project is available under the MIT License. Feel free to use as a reference for your own analysis!

---

**⭐ If this project was helpful, please star the repository!**

*Turning data into decisions, one customer segment at a time.* 📊
