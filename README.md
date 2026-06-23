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

# Mutual Fund Analytics Capstone Project

## Overview

This project focuses on Mutual Fund Analytics using Python, Pandas, SQL, and SQLite. The objective is to perform data ingestion, cleaning, validation, database design, and analytical reporting on mutual fund datasets.

## Tools & Technologies

* Python
* Pandas
* NumPy
* SQLAlchemy
* SQLite
* Jupyter Notebook
* Matplotlib
* Seaborn
* Plotly

## Project Structure

* data/raw/ - Original datasets
* data/processed/ - Cleaned datasets
* notebooks/ - Analysis notebooks
* sql/ - Database schema and SQL queries
* dashboard/ - Dashboard files
* reports/ - Project reports


## Day 2: Data Cleaning & SQLite Database Design

### Completed Tasks

* Cleaned NAV history dataset
* Cleaned investor transactions dataset
* Cleaned scheme performance dataset
* Designed SQLite database schema
* Loaded cleaned datasets into SQLite database
* Created analytical SQL queries
* Prepared data dictionary

### Deliverables

* clean_nav_history.py
* clean_transactions.py
* clean_performance.py
* load_to_sqlite.py
* schema.sql
* queries.sql
* data_dictionary.md
* bluestock_mf.db

## Database Tables

* dim_fund
* fact_nav
* fact_transactions
* fact_performance
* dim_benchmark

## Author

Swapnali Kamble