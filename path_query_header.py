from fastapi import FastAPI, Header
from typing import Optional

app = FastAPI()

# Example 1: Path Parameter
@app.get("/numbers/{number1}")
async def read_item(number1: int):
    return {"number1": number1}

# Example 2: Query Parameter (optional)
@app.get("/items/")
async def read_items(number1: Optional[int]=0, number2: int = 10):
    return {"number1": number1, "number2": number2}

# Example 3: Header Parameter
@app.get("/req_headers/")
def req_header_param(number1: str = Header(...)): #... for required value 
    return {"number1": number1}


@app.get("/optional_headers/")
def optional_header_param(number1: str = Header(None)):# None for optional value 
    return {"number1": number1}