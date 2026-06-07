# Uber Eats Bangalore Restaurant Intelligence & Decision Support System

A SQL-powered Decision Support System built using Python, Pandas, SQLite, and Streamlit to analyze Uber Eats Bangalore restaurant and order data. The system provides business insights through dynamic filtering and SQL-based analytics.

---

## Project Overview

Uber Eats operates a large-scale restaurant marketplace where business performance depends on factors such as location, pricing, cuisine selection, customer ratings, online ordering availability, and table booking services.

This project transforms raw restaurant and order data into actionable business insights using SQL-based analytics. It helps users explore restaurant performance, customer behavior, pricing patterns, cuisine trends, and revenue metrics.The application presents results as clean tabular DataFrame outputs in Streamlit, without using charts or visualizations.

---

## Features
### Restaurant Analytics

* Restaurant performance
* Ratings and cost analysis
* Popular cuisines
* Location-based analysis
* Online order trends
* Table booking trends
  
### Order Analytics

* Average order value
* Discount usage
* Payment methods
* Customer behavior
* Order segmentation
* Revenue trends
* Restaurant performance

### Business Intelligence (SQL Q&A)

* Predefined questions
* SQL-driven insights
* Automated analysis results
* Decision-making support

---

## Workflow

### 1. Data Collection

* Restaurant dataset (CSV)
* Order dataset (JSON)

### 2. Data Cleaning & Transformation

* Removed duplicates
* Handled missing values
* Cleaned categorical values
* Standardized restaurant names
* Converted rating values to numeric format
* Converted cost values to numeric format
* Prepared structured dataset for SQL analysis

### 3. Database Creation

* Loaded cleaned data into SQLite
* Created structured tables for analysis
* Used SQL for all business queries

### 4. Streamlit Application

#### Page 1: Dynamic Filtering Dashboard

* Filter by Location
* Filter by Restaurant Name 
* Filter by Cuisine
* Filter by Rating
* Filter by Cost for Two
* Filter by Online Order Availability
* Filter by Table Booking Availability


Workflow:

* User selects one or multiple filters in sidebar
* SQL query dynamically updates based on the selected filters
* Matching records are retrieved from the database
* Result is displayed in Pandas DataFrame

---

#### Page 2: Restaurant Analytics Q&A

* Predefined business questions
* SQL queries mapped to each question
* Results displayed as DataFrames

Example insights:

* Top-rated restaurants
* Popular cuisines
* Location performance analysis

---

#### Page 3: Order Analytics Q&A

* SQL analysis on order data
* Answers business questions
* Results shown as DataFrames

Metrics:

* Average Order Value
* Discount usage
* Payment methods
* Customer ordering patterns
* Revenue trends
* Restaurant performance

---

## Technology Stack

* Python
* Pandas
* NumPy
* SQL
* SQLite
* Streamlit

---

## Project Structure

```text 
Uber_Eats_data.csv
orders.json
uber_eats.ipynb
uberstream.py
uberbase.db
requirements.txt
README.md
```
| File | Purpose |
|---|---|
| `Uber_Eats_data.csv` | Raw dataset |
| `orders.json` | Raw dataset |
| `uber_eats.ipynb` | Data cleaning, transformation, and analysis |
| `uberstream.py` | Complete Streamlit application |
| `uberbase.db` | SQLite database |
| `requirements.txt` | Required Python packages |
| `README.md` | Setup and usage instructions |

---
## Required Packages

The application uses:
```text
streamlit  
pandas  
numpy
``` 

All required packages are available in `requirements.txt`.

Install dependencies:

```bash
pip install -r requirements.txt
```

## Installation
### Windows

Open Command Prompt or PowerShell in the extracted project folder:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run uberstream.py
```

### Ubuntu / Linux / macOS

Open Terminal in the extracted project folder:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run uberstream.py
```

Once the application starts, Streamlit displays a local URL such as:

```text
http://localhost:8501
```
Open it in your browser.

## Skills Demonstrated
* Data Cleaning
* Data Transformation
* SQL Queries
* Database Management
* Dynamic SQL Filtering
* Business Insights
* Streamlit Development
---

## Business Value

* Helps in making better business decisions
* Identifies top-performing restaurants
* Understands customer behavior
* Analyzes pricing and discounts
* Revenue analysis
* Helps improve restaurant performance

---
