
import csv


file_path = "data/input/customers.csv"

def read_customer_file(file_path):
    records = []
    expected_columns = {
        "customer_id",
        "name",
        "email",
        "age",
        "country"
    }
    

    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        actual_columns = set(reader.fieldnames) 
        missing_columns = expected_columns - actual_columns
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")
        for row in reader:
            records.append(row)
         
    return records, expected_columns, actual_columns,missing_columns

print("Reading customer file:")
customer_records, expected_columns, actual_columns, missing_columns = read_customer_file(file_path)
print("Expected columns:", expected_columns)
print("Actual columns:", actual_columns)
print("Missing columns:", missing_columns)
for customer in customer_records:
    print(customer)