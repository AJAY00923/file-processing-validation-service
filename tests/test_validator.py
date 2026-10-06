import pytest


from file_validator.validator import validate_customer


def test_validate_customer_returns_no_errors():
    customer = {
        "customer_id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "age": 30,
        "country": "USA"
    }
    errors = validate_customer(customer)
    assert errors == []


def test_invalid_age_returns_error():
    customer = {
        "customer_id":101,
        "name": "John Smith",
        "email": "john@gmail.com",
        "age": 130,
        "country": "US"
    }
    errors = validate_customer(customer)
    assert len(errors) == 1
    assert "age must be an integer between 0 and 120." in errors

@pytest.mark.parametrize(
    "age, should_be_valid",
    [
        (25, True),
        (0, True),
        (120, True),
        (-1, False),
        (121, False),
    ]
)
def test_age_boundaries(age, should_be_valid):
    customer = {
        "customer_id": 101,
        "name": "John Smith",
        "email": "john@gmail.com",
        "age": age,
        "country": "US"
    }
    errors = validate_customer(customer)
    if should_be_valid:
        assert len(errors) == 0
    else:
        assert "age must be an integer between 0 and 120." in errors

def test_multiple_invalid_fields_returns_all_errors():
    customer = {
        "customer_id": -5,
        "name": "",
        "email": "invalidemail",
        "age": 150,
        "country": ""
    }
    errors = validate_customer(customer)
    assert len(errors) == 5
    assert "customer_id must be a positive integer." in errors
    assert "name must be a non-empty string." in errors
    assert "email must be a valid email address." in errors
    assert "age must be an integer between 0 and 120." in errors
    assert "country must be a non-empty string." in errors

def test_whitespace_name_and_country_return_errors():
    customer = {
        "customer_id": 1,
        "name": "   ",
        "email": "john@gmail.com",
        "age": 30,
        "country": "   "
    }
    errors = validate_customer(customer)
    assert len(errors) == 2
    assert "name must be a non-empty string." in errors
    assert "country must be a non-empty string." in errors
@pytest.mark.parametrize(
    "email",
    [
        "@gmail.com",
        "john@",
        "john@@gmail.com",
        "invalidemail.com",
        ],
)
def test_invalid_email_formats(email):
    customer = {
        "customer_id": 1,
        "name": "John Doe",
        "email": email,
        "age": 30,
        "country": "USA"
    }
    errors = validate_customer(customer)
    assert len(errors) == 1
    assert "email must be a valid email address." in errors
