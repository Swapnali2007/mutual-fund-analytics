# Mutual Fund Analytics Capstone Project

## Day 1 - Project Setup & Data Ingestion

### Completed Tasks
- Created project folder structure
- Installed required dependencies
- Loaded all 10 datasets using Pandas
- Performed initial data quality checks
- Fetched live NAV data using mfapi.in API
- Retrieved NAV data for 5 key mutual fund schemes
- Analyzed fund master dataset
- Validated AMFI codes against NAV history

### Data Quality Summary
- Successfully loaded all 10 datasets
- Total Mutual Fund Schemes: 40
- NAV History Records: 46,000
- Investor Transactions Records: 32,778
- All AMFI codes validated successfully
- No missing AMFI references found

### Deliverables
- data_ingestion.py
- live_nav_fetch.py
- amfi_validation.py
- requirements.txt
- 01_data_ingestion.ipynb