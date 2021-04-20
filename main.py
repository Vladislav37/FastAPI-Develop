from enum import Enum
from fastapi import FastAPI
from typing import Optional
import get_functions  
import post_functions 

app = FastAPI()

get_functions.func_get_items(app)
get_functions.func_read_file(app)
get_functions.read_file_from_db(app)

post_functions.create_element(app)
post_functions.create_element_with_query(app)

@app.put("/put_items")
async def root():
    return {"message": "Put"}

@app.delete("/delete_items")
async def root():
    return {"message": "Delete"}

