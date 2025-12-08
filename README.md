# 💰 E-Commerce Customer Analytics & Revenue Optimization

> Analyzed 60,000+ transactions to identify high-value customer segments and $1.21M retention opportunity through data-driven RFM segmentation.

![MySQL](https://img.shields.io/badge/MySQL-8.0-blue) ![Tableau](https://img.shields.io/badge/Tableau-2024-orange) ![Excel](https://img.shields.io/badge/Excel-Analysis-green) ![Status](https://img.shields.io/badge/Status-Complete-success)

---

## 🎯 Project Summary

Built end-to-end customer analytics system to help an e-commerce business understand customer behavior, prioritize marketing efforts, and maximize revenue retention.

### **Key Results**
- 💎 **Top 17% of customers generate 61% of revenue ($5.6M)** - Champions segment drives majority of sales
- 🚨 **Identified 1,286 high-value at-risk customers** worth $1.21M in potential recovery revenue
- 📊 **Created 7 strategic customer segments** for targeted marketing campaigns
- 💰 **Built business case showing 8.5x ROI** for retention campaigns ($1.21M benefit vs $142K cost)

---

## 🛠️ Tools & Technologies

- **Database:** MySQL - RFM calculations, customer segmentation, revenue analysis
- **Visualization:** Tableau - Interactive dashboard with drill-down capabilities  
- **Financial Modeling:** Excel - ROI calculations, campaign cost projections
- **Data Processing:** Python - Data generation and preprocessing

---

## 📊 What I Built

### **1. MySQL Customer Segmentation (RFM Analysis)**

Created views to calculate three key customer metrics:
- **Recency:** Days since last purchase
- **Frequency:** Total number of orders
- **Monetary:** Total lifetime spend

Classified 15,000 customers into 7 segments:

| Segment | Customers | % of Total | Revenue | % of Revenue | Strategy |
|---------|-----------|------------|---------|--------------|----------|
| **Champions** | 2,616 | 17.4% | $5.62M | **60.8%** | VIP perks, exclusive access |
| **Big Spenders** | 1,755 | 11.7% | $1.24M | 13.4% | Upsell premium products |
| **Loyal** | 351 | 2.3% | $629K | 6.8% | Reward loyalty programs |
| **Promising** | 1,809 | 12.1% | $440K | 4.8% | Nurture with engagement |
| **At Risk** | 112 | 0.8% | $44K | 0.5% | **Win-back campaigns** |
| **Need Attention** | 109 | 0.7% | $29K | 0.3% | Re-engagement emails |
| **Lost** | 8,248 | 55.0% | $1.24M | 13.4% | Low-priority reactivation |

**Business Impact:** Champions alone drive more revenue than all other segments combined.

---

### **2. Tableau Interactive Dashboard**

Built 5-panel dashboard tracking:
- 📈 Revenue trends by customer segment over time
- 🥧 Customer distribution across segments
- 💎 High-value customer identification
- 📍 Geographic revenue breakdown
- 📊 Key performance indicators (KPIs)

**Features:**
- Drill-down by time period, location, and segment
- Filter by customer value and purchase recency
- Export-ready reports for stakeholders

---

### **3. Excel Financial Model**

Built ROI calculator for retention campaigns:

**Assumptions:**
- 1,286 high-value customers at risk (>$500 LTV, 90+ days inactive)
- Average recovery value: $942 per customer
- Campaign cost: $110 per customer
- Expected success rate: 30%

**Results:**
- Total potential value: **$1.21M**
- Campaign investment: **$142K**
- Expected return: **$386K**
- **ROI: 8.5x** (or 272% return)

---

## 📁 Project Files
```
ecommerce-analytics/
├── Data/
│   ├── customers.csv         # 15,000 customer records
│   ├── orders.csv            # 60,000 order transactions
│   ├── products.csv          # 500 product catalog
│   └── order_items.csv       # Order line items
├── SQL/
│   ├── create_database.sql   # Database setup
│   ├── rfm_analysis.sql      # Customer segmentation ⭐
│   └── business_queries.sql  # Key metrics queries
├── Tableau/
│   └── customer_dashboard.twbx   # Interactive dashboard ⭐
├── Excel/
│   └── retention_roi_model.xlsx  # Financial analysis ⭐
├── Python/
│   ├── generate_sample_data.py
│   └── load_to_mysql.py
└── README.md
```

---

## 🚀 How to Run This Project

### **Option 1: View the Dashboard (Easiest)**
1. Download `customer_dashboard.twbx` from `/Tableau` folder
2. Open with [Tableau Public](https://public.tableau.com/app/discover) (free)
3. Explore the interactive visualizations

### **Option 2: Run Full Analysis**
```bash
# 1. Clone repository
git clone https://github.com/AbdelrahmanIsweisa/ecommerce-analytics.git
cd ecommerce-analytics

# 2. Set up MySQL database
mysql -u root -p < SQL/create_database.sql

# 3. Generate sample data
python Python/generate_sample_data.py

# 4. Load data into MySQL
python Python/load_to_mysql.py

# 5. Run RFM analysis
mysql -u root -p ecommerce_analytics < SQL/rfm_analysis.sql

# 6. Open Tableau dashboard or Excel model
```

---

## 💡 Key Insights

### **Finding #1: Revenue Concentration**
- Top 29% of customers (Champions + Big Spenders) generate **74% of revenue**
- Average Champion spends **$2,149** vs. $211 for Lost customers (10x difference)

### **Finding #2: Retention Opportunity**
- 1,286 "Loyal" and "Big Spender" customers haven't purchased in 90+ days
- Historical data shows 30% will respond to targeted campaigns
- Low-cost intervention now prevents expensive reacquisition later

### **Finding #3: Segment-Specific Strategies**
- **Champions:** Already engaged - focus on retention and referrals
- **At Risk:** Act now - personalized offers before they churn
- **Lost:** Low ROI - reallocate budget to higher-value segments


## 📈 Sample Visualizations

![Revenue by Segment](images/revenue_by_segment.png)
*Champions segment dominates total revenue*

![Customer Segmentation](images/customer_segments.png)
*Distribution of customers across 7 strategic segments*

![At-Risk Analysis](images/high_value_at_risk.png)
*High-value customers who need immediate attention*

---

## 🎓 Skills Demonstrated

- **SQL:** Window functions, CTEs, views, joins, aggregations
- **Business Analytics:** RFM segmentation, customer lifetime value, churn analysis
- **Data Visualization:** Dashboard design, storytelling with data, KPI tracking
- **Financial Modeling:** ROI calculations, cost-benefit analysis, scenario planning
- **Business Communication:** Translating technical findings into actionable recommendations

---

## 🔮 Next Steps

If I had more time, I'd add:
- **Cohort analysis** to track retention rates by signup month
- **Product recommendation engine** using market basket analysis
- **Predictive churn model** using machine learning (logistic regression)
- **A/B test framework** to measure campaign effectiveness
- **Automated email triggers** when customers hit "At Risk" status

---

## 👤 About Me

**Abdelrahman Isweisa**  
MIS Student | Business Analytics Enthusiast | Data-Driven Problem Solver

- 📧 Email: Abdelrahman_Isweisa@student.uml.edu
- 💼 LinkedIn: [linkedin.com/in/abdelrahmanisweisa](https://www.linkedin.com/in/abdelrahmanisweisa)
- 📍 Location: Shrewsbury, MA

*Currently seeking entry-level Business Analyst, Operations Analyst, or Customer Success Analyst roles.*

---

## 📄 License

This project is available under the MIT License. Feel free to use this as a template for your own analysis!

---

**⭐ If this project helped you learn something new, please star the repo!**

*Built with real-world business impact in mind* 💼
