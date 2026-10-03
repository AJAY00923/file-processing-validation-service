def parse_customer(row):
    """
    Parse a raw customer row into appropriate Python data types.

    Args:
        row (dict): Customer data containing customer_id, name,
            email, age, and country.
    """
    return {
        "customer_id": int(row["customer_id"]),
        "name": row["name"],
        "email": row["email"],
        "age": int(row["age"]),
        "country": row["country"],
    }


