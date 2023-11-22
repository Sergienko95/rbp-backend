from pathlib import Path
import fastapi
from devtools import debug

from db import Review, get_saved_reviews, delete_all_reviews, save_review

from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = fastapi.FastAPI()

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

""" 
    1.   Сделать запрос на сервак и получить все отзовы.
    1.5. Сделать запрос на сервер и создать отзыв.
    2.   Сделать запрос на сервак и получить один отзыв.
    3.   Сделать запрос на сервак и обновить отзыв один.
    4.   Сделать запрос на сервак и удалить отзыв один.
"""


@app.get("/", response_class=HTMLResponse)
def handle_index():
    _app_py = Path(__file__)
    DIR_REPO = _app_py.parent
    index_html = DIR_REPO / "index.html"
    with index_html.open("r") as stream:
        return stream.read()


@app.get("/reviews")
async def handle_get_all_reviews():
    reviews = await get_saved_reviews()
    return reviews


@app.delete("/reviews", status_code=204)
async def handle_delete_all_reviews():
    await delete_all_reviews()


@app.post("/reviews", status_code=201)
async def handle_create_review(review: Review = fastapi.Body()):
    debug(review)
    await save_review(review)
    return review


@app.get("/reviews/{review_id}")
async def handle_get_all_reviews(
    *, review_id: int = fastapi.Path()
):  # TODO: переименовать функцию
    debug(review_id)
    # TODO: что будет, если сохраненных отзывов не будет -> 404
    # TODO: что будет, если review_id будут разные
    # TODO: что будет, если придет запрос на review_id, которого нет (что будет с серваком) -> 404
    reviews = await get_saved_reviews()
    for review in reviews:
        if review.id == review_id:
            break
    else:
        return JSONResponse(
            status_code=404,
            content={"message": f"review with id={review_id} not found"},
        )
    return review


@app.delete("/reviews/{review_id}", status_code=204)
async def handle_delete_all_reviews(
    *, review_id: int = fastapi.Path()
):  # TODO: переименовать функцию
    debug(review_id)
    # TODO: что будет, если сохраненных отзывов не будет -> 404
    # TODO: что будет, если review_id будут разные
    # TODO: что будет, если придет запрос на review_id, которого нет (что будет с серваком) -> 404
    await delete_all_reviews()


@app.put("/reviews/{review_id}")
async def handle_create_review(
    *, review: Review = fastapi.Body(), review_id: int = fastapi.Path()
):  # TODO: переименовать функцию
    debug(review, review_id)
    # TODO: что будет, если сохраненных отзывов не будет -> 404
    # TODO: что будет, если review_id будут разные
    # TODO: что будет, если придет запрос на review_id, которого нет (что будет с серваком) -> 404
    await save_review(review)
    return review
