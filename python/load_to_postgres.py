import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection details
DB_USER = "postgres"
DB_PASSWORD = "YOUR_POSTGRES_PASSWORD"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "pricing_sales_analytics"

# Create database connection
connection_string = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(connection_string)

# Load cleaned dataset
df = pd.read_csv("data/clean_sales_data.csv")

# Convert date column
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Load data into PostgreSQL
df.to_sql(
    "sales",
    engine,
    if_exists="replace",
    index=False
)

print("Data successfully loaded into PostgreSQL!")
print("Rows loaded:", len(df))
print("Columns loaded:", len(df.columns))