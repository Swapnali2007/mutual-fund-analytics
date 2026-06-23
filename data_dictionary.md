# Data Dictionary

## dim_fund
- amfi_code : Unique Scheme Code
- fund_house : Mutual Fund House
- scheme_name : Scheme Name
- category : Fund Category
- sub_category : Fund Sub Category

## fact_nav
- amfi_code : Scheme Code
- date : NAV Date
- nav : Net Asset Value

## fact_transactions
- investor_id : Investor ID
- transaction_date : Transaction Date
- transaction_type : SIP/Lumpsum/Redemption
- amount_inr : Transaction Amount

## fact_performance
- return_1yr_pct : 1 Year Return
- return_3yr_pct : 3 Year Return
- sharpe_ratio : Risk Adjusted Return

## dim_benchmark
- index_name : Benchmark Index
- close_value : Closing Index Value