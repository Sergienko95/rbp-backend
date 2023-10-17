import fastapi
from devtools import debug

from function import Review, get_saved_reviews, delete_all_reviews, save_review

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
    reviews = await get_saved_reviews()
    return reviews


@app.delete("/reviews", status_code=204)
async def handle_delete_all_reviews():
    await delete_all_reviews()


# Сделать post запрос на /reviews
@app.post("/reviews", status_code=201)
async def handle_create_review(review: Review = fastapi.Body()):
    debug(review)
    await save_review(review)
    return review
