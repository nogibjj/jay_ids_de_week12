---
title: "SQLite Lab"
format: html
---

## SQLite Lab

[![CI](https://github.com/yourusername/US_birth_ETL_Project/actions/workflows/cicd.yml/badge.svg)](https://github.com/yourusername/US_birth_ETL_Project/actions/workflows/cicd.yml)

# Project Overview

This project focuses on the process of extracting, transforming, loading (ETL), and querying U.S. birth data. The dataset comes from a CSV file, `US_birth.csv`, which contains records of birth counts from different years, months, and days of the week. The project includes Python scripts to automate the ETL processes using Databricks, as well as unit tests using `pytest`.

## Project Structure

Here’s an overview of the project structure:

```{.yaml}
├── Dockerfile
├── LICENSE
├── Makefile
├── README.qmd
├── US_birth.csv
├── main.py
├── mylib
│   ├── __init__.py
│   ├── __pycache__
│   ├── extract.py
│   ├── query.py
│   └── transform_load.py
├── requirements.txt
├── setup.sh
└── test_main.py
Requirements
Before running the project, make sure you have the following dependencies installed:

Python 3.9+
requests - for fetching data from a URL.
pytest - for unit testing.
databricks-sql-connector - for connecting to Databricks.
WITH birth_stats AS (
    SELECT 
        year,  -- Group by year to get stats per year
        month,  -- Group by month to get stats per month
        AVG(births) AS avg_births,  -- Average number of births per month
        SUM(births) AS total_births  -- Total number of births per month
    FROM default.us_birth_data  -- Your birth data table
    GROUP BY year, month
)

SELECT *
FROM default.us_birth_data
JOIN birth_stats
ON default.us_birth_data.year = birth_stats.year
AND default.us_birth_data.month = birth_stats.month
ORDER BY birth_stats.total_births DESC;  -- Rank by total births
Query Explanation
CTE birth_stats: This common table expression groups births by year and month to calculate:

The average number of births for each year-month combination.
The total number of births for each year-month combination.
Join: The birth_stats CTE is then joined with the original us_birth_data table, enriching each record with aggregated statistics for its respective year and month.

Ranking: Finally, the results are ordered by the total number of births, providing insights into which year-month combinations had the highest birth counts.

This query helps identify trends in birth counts across different years and months, providing useful insights for demographic analysis.

Sample output:
Row(year=2000, month=1, avg_births=11234.5, total_births=22469)
Row(year=2000, month=2, avg_births=10500.7, total_births=21001)

Here's how you can write the README in a .qmd (Quarto Markdown) file format. This will include the same structure as the earlier README with the necessary Markdown elements for Quarto.

qmd
Copy code
---
title: "SQLite Lab"
format: html
---

## SQLite Lab

[![CI](https://github.com/yourusername/US_birth_ETL_Project/actions/workflows/cicd.yml/badge.svg)](https://github.com/yourusername/US_birth_ETL_Project/actions/workflows/cicd.yml)

# Project Overview

This project focuses on the process of extracting, transforming, loading (ETL), and querying U.S. birth data. The dataset comes from a CSV file, `US_birth.csv`, which contains records of birth counts from different years, months, and days of the week. The project includes Python scripts to automate the ETL processes using Databricks, as well as unit tests using `pytest`.

## Project Structure

Here’s an overview of the project structure:

```{.yaml}
├── Dockerfile
├── LICENSE
├── Makefile
├── README.qmd
├── US_birth.csv
├── main.py
├── mylib
│   ├── __init__.py
│   ├── __pycache__
│   ├── extract.py
│   ├── query.py
│   └── transform_load.py
├── requirements.txt
├── setup.sh
└── test_main.py
Requirements
Before running the project, make sure you have the following dependencies installed:

Python 3.9+
requests - for fetching data from a URL.
pytest - for unit testing.
databricks-sql-connector - for connecting to Databricks.
Complex Query
Here’s the complex query used in this project:

sql
Copy code
WITH birth_stats AS (
    SELECT 
        year,  -- Group by year to get stats per year
        month,  -- Group by month to get stats per month
        AVG(births) AS avg_births,  -- Average number of births per month
        SUM(births) AS total_births  -- Total number of births per month
    FROM default.us_birth_data  -- Your birth data table
    GROUP BY year, month
)

SELECT *
FROM default.us_birth_data
JOIN birth_stats
ON default.us_birth_data.year = birth_stats.year
AND default.us_birth_data.month = birth_stats.month
ORDER BY birth_stats.total_births DESC;  -- Rank by total births
Query Explanation
CTE birth_stats: This common table expression groups births by year and month to calculate:

The average number of births for each year-month combination.
The total number of births for each year-month combination.
Join: The birth_stats CTE is then joined with the original us_birth_data table, enriching each record with aggregated statistics for its respective year and month.

Ranking: Finally, the results are ordered by the total number of births, providing insights into which year-month combinations had the highest birth counts.

This query helps identify trends in birth counts across different years and months, providing useful insights for demographic analysis.

Sample output:
{.yaml}
Copy code
Row(year=2000, month=1, avg_births=11234.5, total_births=22469)
Row(year=2000, month=2, avg_births=10500.7, total_births=21001)
Check Format and Test Errors
Format code: make format
Lint code: make lint
Test code: make test
References
Databricks SQL Documentation
Databricks SQL Connector for Python
SQLite Documentation