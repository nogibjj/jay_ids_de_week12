"""
Test goes here

"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query


def test_extract():
    test_1 = extract()
    assert test_1 is not None


def test_load():
    """test load"""
    test_2 = load()
    assert test_2 == "db loaded or already loaded"


def test_query():
    """test query"""
    test_3 = query()
    assert test_3 == "query successful"


if __name__ == "__main__":
    test_extract()
    test_load()
    test_query()
