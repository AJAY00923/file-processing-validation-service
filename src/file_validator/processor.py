from file_validator.parser import parse_customer
from file_validator.validator import validate_customer


def process_customers(records):
    valid = []
    rejected = []
    seen_ids = set()

    for record in records:
        try:
            customer = parse_customer(record)
        except ValueError as e:
            rejected.append({"record": record, "errors": [str(e)]})
            continue

        if customer["customer_id"] in seen_ids:
            rejected.append({"customer": customer, "errors": ["Duplicate customer_id"]})
            continue
        else:
            seen_ids.add(customer["customer_id"])

        errors = validate_customer(customer)

        if errors:
            rejected.append({"customer": customer, "errors": errors})
        else:
            valid.append(customer)

    return valid, rejected