from file_validator.processor import process_customers

def test_process_customers():
    #----------ARRANGE----------
    records = [
        {
            "customer_id": "1",
            "name": "John Doe",
            "email": "john.doe@example.com",
            "age": "30",
            "country": "USA"
            },
        {
            "customer_id": "2",
            "name": "",
            "email": "invalidemail",
            "age": "25",
            "country": "Canada"
            },
    ]
    #---------ACT----------
    valid, rejected = process_customers(records)
    #---------ASSERT----------
    assert len(valid) == 1
    assert len(rejected) == 1


def test_process_customers_with_malformed_records():
        #----------ARRANGE----------
    records = [
        {
          "customer_id" : "1",
          "name": "john doe",
          "email": "john.doe@example.com",
          "age": "30",
          "country": "USA"
         },
        {
            "customer_id": "2",
            "name": "",
            "email": "invalidemail",
            "age": "abc",  # Invalid age
           "country": "Canada"
            },
        {
            "customer_id": "3",
            "name": "Jane Smith",
            "email": "jane.smith@example.com",
            "age": "28",
            "country": "USA"
        }
    ]
    #---------ACT----------
    valid,rejected = process_customers(records)
    #---------ASSERT----------
    assert len(valid) == 2
    assert len(rejected) == 1

    assert rejected[0]["record"]["customer_id"] == "2"
    assert len(rejected[0]["errors"]) >= 1

def test_process_customers_with_duplicate_ids():
    #----------ARRANGE----------
    records = [
        {
            "customer_id": "1",
            "name": "John Doe",
            "email": "john.de@gmail.com",
            "age": "30",
            "country": "USA"
        },
        {
            "customer_id": "1",  # Duplicate ID
            "name": "Jane Smith",
            "email": "jane.smith@gmail.com",
            "age": "28",
            "country": "USA"
        }
    ]
    #---------ACT----------
    valid, rejected = process_customers(records)
    #---------ASSERT----------
    assert len(valid) == 1
    assert len(rejected) == 1