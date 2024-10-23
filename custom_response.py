from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, PlainTextResponse,HTMLResponse

app = FastAPI()

# Example 1: Returning a custom JSON response
@app.get("/custom-json/")
async def custom_json_response():
    maro_content = {"message": "This is Yashvi Savaj"}
    return JSONResponse(content=maro_content, status_code=200)

# Example 2: Returning a custom plain text response
@app.get("/custom-text/")
async def custom_text_response():
    content = "This is a custom plain text response"
    return PlainTextResponse(content=content, status_code=200)

# Example 3: Returning a custom HTML response
@app.get("/custom-html/")
async def custom_html_response():
    html_content = """
    <html>
        <head>
            <title>Custom HTML Response</title>
        </head>
        <body>
            <h1>Hello, FastAPI!</h1>
            <p>This is a custom HTML response</p>
        </body>
    </html>
    """
    print(html_content)
    return HTMLResponse(content=html_content)