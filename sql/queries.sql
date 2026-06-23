-- 1 Top 5 Fund Houses by Number of Schemes
SELECT fund_house, COUNT(*) AS total_schemes
FROM dim_fund
GROUP BY fund_house
ORDER BY total_schemes DESC
LIMIT 5;

-- 2 Average NAV
SELECT AVG(nav) AS avg_nav
FROM fact_nav;

-- 3 Highest NAV
SELECT MAX(nav) AS highest_nav
FROM fact_nav;

-- 4 Transaction Count by Type
SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- 5 Transactions by State
SELECT state, COUNT(*)
FROM fact_transactions
GROUP BY state
ORDER BY COUNT(*) DESC;

-- 6 Funds with Expense Ratio < 1%
SELECT scheme_name, expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1;

-- 7 Average 1 Year Return
SELECT AVG(return_1yr_pct)
FROM fact_performance;

-- 8 Negative Sharpe Ratio Funds
SELECT amfi_code, sharpe_ratio
FROM fact_performance
WHERE sharpe_ratio < 0;

-- 9 Benchmark Count
SELECT index_name, COUNT(*)
FROM dim_benchmark
GROUP BY index_name;

-- 10 Total Transactions Amount
SELECT SUM(amount_inr)
FROM fact_transactions;