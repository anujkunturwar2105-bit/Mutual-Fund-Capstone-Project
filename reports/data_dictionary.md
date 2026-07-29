# Mutual Fund Data Dictionary

## fund_master
- amfi_code : Unique AMFI Scheme Code
- fund_house : Mutual Fund Company
- scheme_name : Scheme Name
- category : Fund Category
- sub_category : Sub Category
- plan : Direct/Regular
- benchmark : Benchmark Index
- expense_ratio_pct : Expense Ratio
- risk_category : Risk Level

## nav_history
- amfi_code : Scheme Code
- date : NAV Date
- nav : Net Asset Value

## investor_transactions
- transaction_id : Transaction ID
- investor_id : Investor ID
- transaction_type : Purchase/Redemption
- amount : Transaction Amount

## scheme_performance
- returns_1y : One Year Return
- returns_3y : Three Year Return
- returns_5y : Five Year Return