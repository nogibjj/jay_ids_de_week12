"""Query the database"""

import os
from dotenv import load_dotenv
from databricks import sql

complex_query = """
WITH birth_stats AS (
    SELECT 
        year,  -- Group by year to get birth stats per year
        month,  -- Group by month to get birth stats per month
        AVG(births) AS avg_births,  -- Average number of births per month
        SUM(births) AS total_births  -- Total number of births per month
    FROM default.us_birth_data  
    GROUP BY year, month
)

SELECT *
FROM default.us_birth_data
JOIN birth_stats
ON default.us_birth_data.year = birth_stats.year
AND default.us_birth_data.month = birth_stats.month
ORDER BY birth_stats.total_births DESC;  
"""


def query():
    """Query the database for birth stats from the US Birth Data table"""
    load_dotenv()  # Load environment variables from .env file

    # Establish connection to the database using Databricks SQL connector
    with sql.connect(
        server_hostname=os.getenv("SERVER_HOSTNAME"),
        http_path=os.getenv("HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_KEY"),
    ) as connection:

        with connection.cursor() as cursor:
            # Execute the complex query
            cursor.execute(complex_query)
            result = cursor.fetchall()

            # Print each row of the result
            for row in result:
                print(row)

    return "Query successful"


if __name__ == "__main__":
    query()
