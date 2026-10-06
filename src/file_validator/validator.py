def validate_customer(customer):
    errors = []
    email = customer["email"]
    if not isinstance(customer["customer_id"], int) or customer["customer_id"] <=0:
        errors.append("customer_id must be a positive integer.")
    if not isinstance(customer["name"], str) or not customer["name"].strip():
        errors.append("name must be a non-empty string.")
    if not isinstance(email, str) or email.count("@") != 1:
        errors.append("email must be a valid email address.")
    else:
        local_part, domain = email.split("@")
        if not local_part or not domain:
            errors.append("email must be a valid email address.")
    if not isinstance(customer["age"], int) or customer["age"] < 0 or customer["age"] > 120:
        errors.append("age must be an integer between 0 and 120.")
    if not isinstance(customer["country"], str) or not customer["country"].strip():
        errors.append("country must be a non-empty string.")
    return errors