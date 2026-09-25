# Pricing & Sales Analytics Dashboard

## 📊 Project Overview

The Pricing & Sales Analytics Dashboard is an end-to-end business analytics project designed to analyze sales performance, pricing, discounts, profitability, and regional performance.

The project demonstrates a complete data analytics workflow:

Sales Dataset → Python Data Analysis → PostgreSQL → SQL Business Analysis → Power BI Dashboard

The dashboard provides interactive business insights that can support pricing analysis, sales monitoring, and commercial decision-making.

> **Data Note:** This project uses a synthetic sales dataset created for analytics demonstration and portfolio purposes. It does not use confidential or proprietary company data.

---

## 📸 Dashboard Preview

![Pricing & Sales Analytics Dashboard](powerbi/dashboard_preview.png)

## 🎯 Project Objectives

- Analyze overall sales and profitability.
- Understand the relationship between pricing, discounts, and profit margins.
- Compare sales performance across products, categories, regions, and salespeople.
- Identify high-revenue and high-profit products.
- Monitor monthly sales and profit trends.
- Build an interactive business intelligence dashboard.
- Demonstrate an end-to-end data analytics workflow using Python, SQL, PostgreSQL, and Power BI.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- PostgreSQL
- SQL
- SQLAlchemy
- Power BI
- DAX
- Git / GitHub

---

## 📁 Project Structure

```text
Pricing_Sales_Analytics/
│
├── data/
│   ├── sales_data.csv
│   └── clean_sales_data.csv
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   └── 02_pricing_sales_analysis.ipynb
│
├── python/
│   ├── generate_dataset.py
│   └── load_to_postgres.py
│
├── sql/
│   └── 01_business_analysis.sql
│
├── powerbi/
│   └── Pricing_Sales_Analytics_Dashboard.pbix
│
├── README.md
└── requirements.txt
