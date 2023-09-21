import fastapi
from devtools import debug

app = fastapi.FastAPI()

""" 
    1.   Сделать запрос на сервак и получить все отзовы.
    1.5. Сделать запрос на сервер и создать отзыв.
    2.   Сделать запрос на сервак и получить один отзыв.
    3.   Сделать запрос на сервак и обновить отзыв один.
    4.   Сделать запрос на сервак и удалить отзыв один.
"""

# Сделать get запрос на /reviews
@app.get("/reviews")
async def handle_get_all_reviews():
    reviews = []
    return reviews


# Сделать post запрос на /reviews
@app.post("/reviews", status_code=201)
async def handle_create_review(review: dict=fastapi.Body(), user_agent: str=fastapi.Header('user-agent')):
    debug (review, user_agent)
    return review


@app.get("/")
async def handle_hello_world():
    return "hello world"


@app.get("/languages")
async def handle_languages():
    return {
        "jana": "python",
    }


@app.get("/favicon.ico")
async def handle_favicon():
    with open("favicon.jpg", "rb") as file_object:
        image = file_object.read()

    return fastapi.Response(
        image,
        media_type="image/jpeg",
    )
