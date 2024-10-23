from fastapi import FastAPI, Cookie, Response, HTTPException

app = FastAPI()

# Endpoint to set a cookie
@app.get("/set-cookie/")
async def set_cookie(color_value:str,my_response: Response):
    my_response.set_cookie(key="color", value=color_value, httponly=True)
    return {"message": f"Cookie 'color' has been set to {color_value}"}

# Endpoint to read a cookie
@app.get("/get-cookie/")
async def get_cookie(color: str = Cookie(None)):
    if color:
        return {"message": f"Hello, {color}!"}
    else:
        raise HTTPException(status_code=404, detail="Cookie not found")

# Endpoint to delete a cookie
@app.get("/delete-cookie/")
async def delete_cookie(response: Response):
    response.delete_cookie(key="color")
    return {"message": "Cookie 'color' has been deleted"}