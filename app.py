import fastapi
from devtools import debug

from db import Review, get_saved_reviews, delete_all_reviews, save_review

app = fastapi.FastAPI()

""" 
    1.   Сделать запрос на сервак и получить все отзовы.
    1.5. Сделать запрос на сервер и создать отзыв.
    2.   Сделать запрос на сервак и получить один отзыв.
    3.   Сделать запрос на сервак и обновить отзыв один.
    4.   Сделать запрос на сервак и удалить отзыв один.
"""


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
async def handle_get_all_reviews(*, review_id: int=fastapi.Path()):  # TODO: переименовать функцию
    debug(review_id)
    # TODO: что будет, если сохраненных отзывов не будет -> 404
    # TODO: что будет, если review_id будут разные 
    # TODO: что будет, если придет запрос на review_id, которого нет (что будет с серваком) -> 404
    reviews = await get_saved_reviews()
    review = reviews[0]
    return review


@app.delete("/reviews/{review_id}", status_code=204)
async def handle_delete_all_reviews(*, review_id: int=fastapi.Path()):  # TODO: переименовать функцию
    debug(review_id)
    # TODO: что будет, если сохраненных отзывов не будет -> 404
    # TODO: что будет, если review_id будут разные 
    # TODO: что будет, если придет запрос на review_id, которого нет (что будет с серваком) -> 404
    await delete_all_reviews()


@app.put("/reviews/{review_id}")
async def handle_create_review(*, review: Review = fastapi.Body(), review_id: int=fastapi.Path()):  # TODO: переименовать функцию
    debug(review, review_id)
    # TODO: что будет, если сохраненных отзывов не будет -> 404
    # TODO: что будет, если review_id будут разные 
    # TODO: что будет, если придет запрос на review_id, которого нет (что будет с серваком) -> 404
    await save_review(review)
    return review