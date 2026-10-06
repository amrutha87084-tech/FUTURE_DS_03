# FUTURE_DS_03
Interactive Bank Marketing Campaign Analysis dashboard built using Python and Power BI.

# Bank Marketing Campaign Analysis – Future Interns Task 3

## 📊 Project Overview

This project was completed as part of the **Future Interns Data Science Internship – Task 3**.

The project focuses on analyzing a bank marketing campaign dataset to understand customer conversion patterns and identify factors associated with successful term-deposit subscriptions.

The analysis was performed using **Python**, and an interactive dashboard was created using **Microsoft Power BI**.

---

## 🎯 Objectives

- Analyze customer and campaign data.
- Calculate key campaign performance metrics.
- Identify factors associated with customer conversion.
- Analyze conversion patterns across different customer segments.
- Build an interactive Power BI dashboard.
- Generate useful business insights from the data.

---

## 📂 Dataset

The project uses the **UCI Bank Marketing Dataset**.

**Dataset:** Bank Marketing – `bank-additional-full.csv`

- Records: **41,188**
- Original columns: **21**
- Target variable: `y`
- `yes` → Customer subscribed to a term deposit
- `no` → Customer did not subscribe

---

## 🛠️ Tools & Technologies

- **Python**
- **Pandas**
- **Microsoft Power BI**
- **DAX**
- **Data Visualization**
- **Exploratory Data Analysis**

---

## 🐍 Python Data Analysis

Python was used for:

- Loading the dataset
- Exploring the data
- Checking missing values
- Analyzing conversion performance
- Job-wise conversion analysis
- Contact-method analysis
- Month-wise conversion analysis
- Previous campaign outcome analysis
- Campaign contact frequency analysis
- Feature engineering
- Creating the cleaned dataset

### Additional Features Created

- `conversion`
- `age_group`
- `campaign_group`
- `previous_contact`
- `month_number`

The processed dataset was exported as:

`marketing_campaign_cleaned.csv`

---

## 📈 Key Performance Indicators

| Metric | Value |
|---|---:|
| Total Customers | 41,188 |
| Successful Conversions | 4,640 |
| Conversion Rate | 11.27% |
| Average Campaign Contacts | 2.57 |

---

## 📊 Power BI Dashboard

The interactive dashboard includes:

- KPI Cards
- Conversion Rate by Month
- Conversion Rate by Education
- Conversion Rate by Previous Campaign Outcome
- Conversion Rate by Campaign Group
- Customer Outcome Analysis
- Count of Outcomes by Job
- Count of Outcomes by Contact Method
- AI Key Influencers
- Interactive Month, Job and Education slicers

---

## 🔍 Key Insights

- The overall campaign conversion rate was **11.27%**.
- **4,640 customers** successfully subscribed to the term deposit.
- Customers with a previous successful campaign outcome showed a much higher observed conversion rate.
- **Cellular** communication had a higher observed conversion rate than telephone communication.
- Conversion generally showed a decreasing pattern as the number of contacts increased.
- Customer segments such as students and retired customers showed relatively high conversion rates.

---

## 💡 Business Recommendations

- Prioritize customers with positive previous campaign outcomes.
- Analyze communication channels to improve campaign effectiveness.
- Avoid excessive repeated contacts without evidence of additional benefit.
- Use customer segmentation to identify potentially responsive groups.
- Use interactive dashboard filters to compare campaign performance across customer segments.

---

## 📁 Project Structure

```text
FUTURE_DS_03/
│
├── data/
│   └── bank-additional-full.csv
│
├── src/
│   └── analysis.py
│
├── output/
│   └── marketing_campaign_cleaned.csv
│
├── report/
│   └── Future_Interns_Task_3_Bank_Marketing_Report.docx
│
└── README.md
