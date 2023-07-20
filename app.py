import fastapi

app = fastapi.FastAPI()

@app.get("/")
async def handle_hello_world():
    return "hello"

@app.get("/favicon.ico")
async def handle_favicon():
    with open("favicon.jpg", "rb") as file_object:
        image = file_object.read()

    return fastapi.Response(image, media_type="image/jpeg")
