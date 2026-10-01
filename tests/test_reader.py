import pytest

from file_validator.reader import read_customer_file


def test_missing_required_columns_raises_error(tmp_path):
    # Create a temporary CSV file with missing required columns
    csv_file = tmp_path / "customers.csv"

    csv_file.write_text(
        "customer_id,name,age\n"
        "1,John Doe,30\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError) as exc_info:
        read_customer_file(csv_file)

    assert "Missing required columns" in str(exc_info.value)


def test_valid_customer_file_returns_records(tmp_path):
    csv_file = tmp_path / "customers.csv"

    csv_file.write_text(
        "customer_id,name,email,age,country\n"
        "101,John Smith,john@gmail.com,32,US\n"
        "102,Sarah Lee,sarah@gmail.com,28,US\n",
        encoding="utf-8",
    )

    records, expected_columns, actual_columns, missing_columns = read_customer_file(
        csv_file
    )

    assert len(records) == 2
    assert records[0]["customer_id"] == "101"
    assert records[0]["name"] == "John Smith"
    assert records[0]["email"] == "john@gmail.com"
    assert records[1]["customer_id"] == "102"
    assert missing_columns == set()