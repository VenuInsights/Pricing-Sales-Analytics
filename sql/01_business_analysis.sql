-- =========================================================
-- PRICING & SALES ANALYTICS
-- Business Analysis SQL Queries
-- =========================================================


-- =========================================================
-- QUERY 1: Overall Business Performance
-- =========================================================

SELECT
    COUNT(*) AS total_orders,
    SUM("Revenue") AS total_revenue,
    SUM("Cost") AS total_cost,
    SUM("Profit") AS total_profit,
    AVG("Profit_Margin") AS average_profit_margin,
    SUM("Quantity") AS total_units_sold,
    AVG("Unit_Price") AS average_unit_price,
    AVG("Discount") AS average_discount
FROM sales;


-- =========================================================
-- QUERY 2: Revenue & Profit by Category
-- =========================================================

SELECT
    "Category",
    SUM("Revenue") AS total_revenue,
    SUM("Profit") AS total_profit,
    SUM("Quantity") AS units_sold
FROM sales
GROUP BY "Category"
ORDER BY total_revenue DESC;


-- =========================================================
-- QUERY 3: Regional Performance
-- =========================================================

SELECT
    "Region",
    SUM("Revenue") AS total_revenue,
    SUM("Profit") AS total_profit,
    SUM("Quantity") AS units_sold,
    AVG("Profit_Margin") AS average_profit_margin
FROM sales
GROUP BY "Region"
ORDER BY total_revenue DESC;


-- =========================================================
-- QUERY 4: Monthly Revenue & Profit
-- =========================================================

SELECT
    DATE_TRUNC('month', "Order_Date") AS month,
    SUM("Revenue") AS total_revenue,
    SUM("Profit") AS total_profit,
    SUM("Quantity") AS units_sold
FROM sales
GROUP BY month
ORDER BY month;


-- =========================================================
-- QUERY 5: Top 10 Products by Revenue
-- =========================================================

SELECT
    "Product",
    SUM("Revenue") AS total_revenue,
    SUM("Profit") AS total_profit,
    SUM("Quantity") AS units_sold,
    AVG("Profit_Margin") AS average_profit_margin
FROM sales
GROUP BY "Product"
ORDER BY total_revenue DESC
LIMIT 10;


-- =========================================================
-- QUERY 6: Salesperson Performance
-- =========================================================

SELECT
    "Salesperson",
    COUNT(*) AS total_orders,
    SUM("Revenue") AS total_revenue,
    SUM("Profit") AS total_profit,
    SUM("Quantity") AS units_sold,
    AVG("Profit_Margin") AS average_profit_margin
FROM sales
GROUP BY "Salesperson"
ORDER BY total_revenue DESC;


-- =========================================================
-- QUERY 7: Discount vs Profitability
-- =========================================================

SELECT
    "Discount",
    COUNT(*) AS total_orders,
    SUM("Revenue") AS total_revenue,
    SUM("Profit") AS total_profit,
    AVG("Profit_Margin") AS average_profit_margin
FROM sales
GROUP BY "Discount"
ORDER BY "Discount";


-- =========================================================
-- QUERY 8: High Revenue but Low Margin Products
-- =========================================================

SELECT
    "Product",
    SUM("Revenue") AS total_revenue,
    SUM("Profit") AS total_profit,
    AVG("Profit_Margin") AS average_profit_margin
FROM sales
GROUP BY "Product"
HAVING AVG("Profit_Margin") < 0.20
ORDER BY total_revenue DESC;


-- =========================================================
-- QUERY 9: Highly Discounted Orders
-- =========================================================

SELECT
    "Discount",
    COUNT(*) AS number_of_orders,
    SUM("Revenue") AS total_revenue,
    SUM("Profit") AS total_profit
FROM sales
WHERE "Discount" >= 0.15
GROUP BY "Discount"
ORDER BY "Discount";


-- =========================================================
-- QUERY 10: Category Profitability
-- =========================================================

SELECT
    "Category",
    SUM("Revenue") AS total_revenue,
    SUM("Cost") AS total_cost,
    SUM("Profit") AS total_profit,
    SUM("Profit") / NULLIF(SUM("Revenue"), 0) AS profit_margin
FROM sales
GROUP BY "Category"
ORDER BY profit_margin DESC;