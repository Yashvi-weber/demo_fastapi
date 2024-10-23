from fastapi import FastAPI,Depends
app = FastAPI()



def sum(a:int,b:int):
    return a+b


@app.get("/sum")
def get_sum(answer:int=Depends(sum)):
    return f"the answer of the two number is {answer}"