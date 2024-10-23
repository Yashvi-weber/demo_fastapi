from fastapi import FastAPI
from src.router.user import user_router
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}   


app.include_router(user_router)