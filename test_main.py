"""
Test goes here
"""

from unittest.mock import patch, MagicMock
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query


def test_extract():
    test_1 = extract()
    assert test_1 is not None


@patch("databricks.sql.connect")
def test_load(mock_connect):
    """test load"""
    # Create a mock connection and cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_connect.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor

    # Simulate an empty database (no rows returned)
    mock_cursor.fetchall.return_value = []

    # Call the load function
    test_2 = load()

    # Ensure the result matches the expected success message
    assert test_2 == "Database loaded or already contains data"


@patch("databricks.sql.connect")
def test_query(mock_connect):
    """test query"""
    # Create a mock connection and cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_connect.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor

    # Simulate query results
    mock_cursor.fetchall.return_value = [("2000", "1", "1", "6", "9083")]

    # Call the query function
    test_3 = query()

    # Ensure the result matches the expected success message
    assert test_3 == "Query successful"


if __name__ == "__main__":
    test_extract()
    test_load()
    test_query()
