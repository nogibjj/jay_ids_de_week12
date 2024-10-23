"""
Transforms and Loads data into the local Databricks database
"""

import csv
import os
import logging
from dotenv import load_dotenv
from databricks import sql


def load(dataset="US_birth.csv"):
    """Transforms and Loads data into the local Databricks database"""

    load_dotenv()  # Load environment variables for connection details

    try:
        # Open the dataset file safely
        with open(dataset, newline="") as csvfile:
            payload = csv.reader(csvfile, delimiter=",")
            next(payload)  # Skip the header row

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

                    # Check if the table is empty
                    cursor.execute("SELECT * FROM us_birth_data")
                    result = cursor.fetchall()

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

                        # Commit the transaction
                        connection.commit()
                    else:
                        print("Data already exists in the database.")
        
        return "Database loaded or already contains data"

    except Exception as e:
        # Log any errors that occur during the process
        logging.error("Error during the data load process: %s", e, exc_info=True)
        return "Data load failed"


if __name__ == "__main__":
    load()
