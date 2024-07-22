import uvicorn
from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from config.settings import port
from app.routes.urls import init_app_url

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get('/')
def get_root():
    return {"root": "root"}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item_price": item.price}


init_app_url(app)

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=port, reload=True)
