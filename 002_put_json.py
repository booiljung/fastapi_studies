from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.put("/items/{item_id}")
def putItem(item_id: int, item: Item):
    return {
        "item_id": item_id,
        "item_name": item
    }
