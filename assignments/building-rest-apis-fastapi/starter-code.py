from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Simple API")

# Sample data for your application
items = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Mouse", "price": 25.50},
]


class Item(BaseModel):
    name: str
    price: float


@app.get("/")
def read_root():
    # TODO: Return a welcome message or API status
    return {"message": "Welcome to the API!"}


@app.get("/items")
def get_items():
    # TODO: Return the full list of items
    return items


@app.post("/items")
def create_item(item: Item):
    # TODO: Create a new item dictionary and add it to the list
    # Make sure the new item includes an id
    return {"message": "Item created"}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    # TODO: Find the item by id and return it
    # If the item does not exist, raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}


# Optional challenge:
# Add an update route and a delete route for full CRUD functionality.
