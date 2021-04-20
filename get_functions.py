from enum import Enum
from typing import Optional

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

class ItemsName(str, Enum):
    vlad = "Vlad"
    foo = "Foo"
    bar = "Bar"

def func_get_items(app):
    @app.get("/items/{item_id}")
    async def get_items(item_id: str, needy: str, q: Optional[str] = None, short: bool = False):
        item = {"item_id": item_id}
        if q:
            item.update({"item_id": item_id, "q": q})
        elif not short:
            item.update(
                {"description": "This is an amazing item that has a long description"}
            )
        else:
            if item_id == ItemsName.vlad:
                item.update({"message": "vladik limonadik", "item_id": item_id})
            elif item_id == ItemsName.foo:
                item.update({"message": "foo again"})
            elif item_id == ItemsName.bar:
                item.update({"message": "friday bar party"})
            else:
                item.update({"message": "i don't know"})    
        return item

def func_read_file(app):
    @app.get("/files/{file_path:path}")
    async def read_file(file_path: str):
        return {"file_path": file_path}

def read_file_from_db(app):
    @app.get("/db_items/")
    async def read_item(skip: int = 1, limit: int = 10):
        return fake_items_db[skip : skip + limit]