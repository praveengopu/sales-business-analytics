-- Sales Business Analytics SQL queries
-- Assumes sales_data is loaded into a SQL table named sales_data.

-- 1. Total revenue and profit
SELECT
    COUNT(*) AS order_count,
    SUM(units) AS total_units,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales_data;

-- 2. Revenue and profit by region
SELECT
    region,
    COUNT(*) AS orders,
    SUM(units) AS units,
    ROUND(SUM(revenue), 2) AS revenue,
    ROUND(SUM(profit), 2) AS profit
FROM sales_data
GROUP BY region
ORDER BY revenue DESC;

-- 3. Revenue and profit by category
SELECT
    category,
    COUNT(*) AS orders,
    ROUND(SUM(revenue), 2) AS revenue,
    ROUND(SUM(profit), 2) AS profit
FROM sales_data
GROUP BY category
ORDER BY revenue DESC;

-- 4. Monthly revenue
SELECT
    EXTRACT(YEAR FROM order_date) AS year,
    EXTRACT(MONTH FROM order_date) AS month,
    ROUND(SUM(revenue), 2) AS revenue
FROM sales_data
GROUP BY EXTRACT(YEAR FROM order_date), EXTRACT(MONTH FROM order_date)
ORDER BY year, month;
