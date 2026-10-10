from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from file_validator.parser import parse_customer
from file_validator.validator import validate_customer
from file_validator.processor import process_customers

app = FastAPI()


class CustomerRequest(BaseModel):
    customer_id: str
    name: str
    email: str
    age: str
    country: str


@app.get("/health")
def health():
    return {"status" : "ok"}



@app.post("/validate")
def validate_customers(customer: CustomerRequest):
    try:
        parsed = parse_customer(customer.model_dump())

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        ) from e

    errors = validate_customer(parsed)

    if errors:
        raise HTTPException(
            status_code=400,
            detail=errors
        )

    return parsed
@app.post("/validate/batch")
def validate_customer_batch(customers: list[CustomerRequest]):
    pass