# run this file with uvicorn via: `uvicorn main:app --reload`

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI! This is a test."}   # the JSON that is returned

# get endpoint for a greeting
@app.get("/greet/{name}")
def greet_user(name: str):
    return {"greeting": f"Hello there, General {name}!"}

# query paramters
# i.e. via http://127.0.0.1:8000/items/?skip=2&limit=10
@app.get("/items/")
def get_items(skip: int = 0, limit: int = 10):
    return {"items": list(range(skip, skip+limit))}

## POST request with JSON Body
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool

# test via Swagger UI: http://127.0.0.1:8000/docs#/ --> "Try it out"
@app.post("/items/")
def create_items(item: Item):
    return {"item": item, "message": "Item created sucessfully!"}



# path parameters with validation, i.e. via http://127.0.0.1:8000/products/42
@app.get("/products/{product_id}")
def read_product(product_id: int):
    if product_id > 100:
        return {"error": f"Product not found (id no. {product_id} > 100)"}
    return {"product_id": product_id, "details": f"This is a sample product with the id {product_id}"}


# error handling
from fastapi import HTTPException

@app.get("/users/{user_id}")   # i.e. http://127.0.0.1:8000/users/1
def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code=404, detail="User not found.")
    return {"user_id": user_id, "name": "John Doe"}


# add response model
class Product(BaseModel):
    id: str
    name: str
    price: float

@app.get("/product/{product_id}", response_model=Product) # via http://127.0.0.1:8000/product/5
def get_product(product_id: int):
    return {"id": product_id, 
            "name": "Sample Product",
            "price": 99.99,
            }