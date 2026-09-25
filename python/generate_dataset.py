import pandas as pd
import numpy as np
from datetime import datetime

# Make results reproducible
np.random.seed(42)

# Number of sales transactions
NUM_RECORDS = 5000

# -----------------------------
# Master data
# -----------------------------

products = {
    "Smart Meter": {
        "category": "Energy Management",
        "price": 8500,
        "cost_percentage": 0.68
    },
    "Advanced Meter": {
        "category": "Energy Management",
        "price": 12500,
        "cost_percentage": 0.65
    },
    "Communication Module": {
        "category": "IoT Devices",
        "price": 4200,
        "cost_percentage": 0.62
    },
    "IoT Gateway": {
        "category": "IoT Devices",
        "price": 15000,
        "cost_percentage": 0.60
    },
    "Data Logger": {
        "category": "Data Solutions",
        "price": 6800,
        "cost_percentage": 0.63
    },
    "Analytics License": {
        "category": "Software",
        "price": 22000,
        "cost_percentage": 0.35
    },
    "Cloud Platform": {
        "category": "Software",
        "price": 35000,
        "cost_percentage": 0.30
    },
    "Energy Monitor": {
        "category": "Energy Management",
        "price": 7200,
        "cost_percentage": 0.64
    },
    "Network Controller": {
        "category": "Networking",
        "price": 18500,
        "cost_percentage": 0.58
    },
    "Smart Sensor": {
        "category": "IoT Devices",
        "price": 5500,
        "cost_percentage": 0.61
    }
}

regions = [
    "North",
    "South",
    "East",
    "West",
    "Central"
]

salespeople = [
    "Aarav",
    "Priya",
    "Rahul",
    "Sneha",
    "Arjun",
    "Kavya",
    "Rohan",
    "Ananya",
    "Vikram",
    "Meera"
]

customers = [f"Customer_{i:04d}" for i in range(1, 501)]

# -----------------------------
# Generate transactions
# -----------------------------

product_names = list(products.keys())

data = []

for i in range(1, NUM_RECORDS + 1):

    product = np.random.choice(product_names)
    product_info = products[product]

    category = product_info["category"]
    base_price = product_info["price"]
    cost_percentage = product_info["cost_percentage"]

    # Random date between Jan 2025 and Dec 2025
    start_date = pd.Timestamp("2025-01-01")
    end_date = pd.Timestamp("2025-12-31")

    random_days = np.random.randint(
        0,
        (end_date - start_date).days + 1
    )

    order_date = start_date + pd.Timedelta(days=int(random_days))

    # Quantity
    quantity = np.random.randint(1, 21)

    # Small natural price variation
    price_variation = np.random.uniform(0.90, 1.10)

    unit_price = round(
        base_price * price_variation,
        2
    )

    # Discount between 0% and 25%
    discount = np.random.choice(
        [0, 0.05, 0.10, 0.15, 0.20, 0.25],
        p=[0.15, 0.20, 0.25, 0.20, 0.15, 0.05]
    )

    # Revenue after discount
    gross_sales = quantity * unit_price

    revenue = gross_sales * (1 - discount)

    # Cost
    cost = (
        quantity
        * unit_price
        * cost_percentage
    )

    # Profit
    profit = revenue - cost

    # Profit margin
    profit_margin = (
        profit / revenue
        if revenue != 0
        else 0
    )

    data.append({
        "Order_ID": f"ORD{i:05d}",
        "Order_Date": order_date,
        "Customer": np.random.choice(customers),
        "Product": product,
        "Category": category,
        "Region": np.random.choice(regions),
        "Salesperson": np.random.choice(salespeople),
        "Quantity": quantity,
        "Unit_Price": round(unit_price, 2),
        "Discount": discount,
        "Revenue": round(revenue, 2),
        "Cost": round(cost, 2),
        "Profit": round(profit, 2),
        "Profit_Margin": round(profit_margin, 4)
    })

# -----------------------------
# Create DataFrame
# -----------------------------

df = pd.DataFrame(data)

# Sort by date
df = df.sort_values("Order_Date")

# Reset index
df = df.reset_index(drop=True)

# -----------------------------
# Save dataset
# -----------------------------

output_path = "data/sales_data.csv"

df.to_csv(
    output_path,
    index=False
)

# -----------------------------
# Display information
# -----------------------------

print("=" * 50)
print("SALES DATASET CREATED SUCCESSFULLY")
print("=" * 50)

print(f"Number of records: {len(df)}")
print(f"Number of columns: {len(df.columns)}")

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 records:")
print(df.head())

print("\nDataset saved to:")
print(output_path)

print("\nBasic statistics:")
print(df[[
    "Quantity",
    "Unit_Price",
    "Discount",
    "Revenue",
    "Cost",
    "Profit",
    "Profit_Margin"
]].describe())