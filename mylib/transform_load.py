"""
Transforms and Loads data into the local Databricks database
"""

import csv
import os
from dotenv import load_dotenv
from databricks import sql


def load(dataset="US_birth.csv"):
    """ "Transforms and Loads data into the local Databricks database"""

    # Load the dataset
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    next(payload)  # Skip the header row

    # Load environment variables for connection details
    load_dotenv()

    # Establish connection to the database
    with sql.connect(
        server_hostname=os.getenv("SERVER_HOSTNAME"),
        http_path=os.getenv("HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_KEY"),
    ) as connection:

        with connection.cursor() as cursor:
            # Create the table if it does not already exist
            cursor.execute(
                """
            CREATE TABLE IF NOT EXISTS us_birth_data (
                year INT,
                month INT,
                date_of_month INT,
                day_of_week INT,
                births INT
            );
            """
            )

            cursor.execute("SELECT * FROM us_birth_data")
            result = cursor.fetchall()

            # Check if the table is empty and load data if necessary
            if not result:
                print("Loading data into the database...")
                insert_query = """
                INSERT INTO us_birth_data (
                    year, month, date_of_month, day_of_week, births
                ) 
                VALUES (?, ?, ?, ?, ?)
                """

                # Insert each row from the CSV into the database
                for row in payload:
                    cursor.execute(insert_query, row)

                connection.commit()
            else:
                print("Data already exists in the database.")

    return "Database loaded or already contains data"


if __name__ == "__main__":
    load()
