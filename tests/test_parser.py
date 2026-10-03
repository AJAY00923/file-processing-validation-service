import pytest

from file_validator.parser import parse_customer


def test_parse_customer_converts_numeric_fields():
    row = {
        "customer_id": "101",
        "name": "John Doe",
        "email": "john@gmail.com",
        "age": "32",
        "country": "US",
    }

    result = parse_customer(row)

    assert isinstance(result["customer_id"], int)
    assert isinstance(result["age"], int)
    assert result["customer_id"] == 101
    assert result["age"] == 32


def test_parse_customer_invalid_age_raises_error():
    row = {
        "customer_id": "102",
        "name": "Jane Smith",
        "email": "jane@gmail.com",
        "age": "abc",
        "country": "US",
    }

    with pytest.raises(ValueError):
        parse_customer(row)


def test_parse_customer_invalid_customer_id_raises_error():
    row = {
        "customer_id": "invalid",
        "name": "Jane Smith",
        "email": "jane@gmail.com",
        "age": "30",
        "country": "US",
    }

    with pytest.raises(ValueError):
        parse_customer(row)
