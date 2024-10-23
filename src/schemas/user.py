from pydantic import BaseModel
from typing import Optional
from datetime import datetime

date = datetime.now()



class User_Create_Schema(BaseModel):
    name: str
    email: str
    password: str


class User_Return_Schema(BaseModel):
    id:str
    name: str
    email: str
    password: str