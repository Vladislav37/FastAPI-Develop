from pydantic import BaseModel
from typing import List, Optional
from fastapi import Query

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

def create_element(app):
    @app.post("/post_items/{item_id}")
    async def create_item(item: Item, item_id:int, q: Optional[str] = Query(..., min_length=2, max_length=4)):
        item_dict = item.dict()
        if item.tax:
            item_dict.update({"price_with_tax": item.tax + item.price})     
        result = {"item_id": item_id, "body": item_dict}
        if q:
            result.update({"q": q})
        return result

def create_element_with_query(app):
    @app.post("/post_query_items/")
    async def create_query_item(item: Item, l: Optional[List[str]] = Query(
            None,
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            alias="item-query",
            min_length=3,
            deprecated=True
    )):
        item_dict = item.dict()
        result = {"body": item_dict}
        if len(l) > 0:
            result.update({"l": l})
        return result