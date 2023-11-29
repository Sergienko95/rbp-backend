from typing import Any
import requests
from devtools import debug
from random import randint
import pytest
from db import Review


# def test_can_review_create_and_get_back(): 
#     send_data_to_server()
#     wait_for_response()
#     if data_are_saved():
#         pass
#     else:
#         raise AssertionError("всё упало")


def test_reviews():
    
    # Проверяю, что сначала отзывов нет
    response = requests.get("http://localhost:8000/reviews")
    assert response.status_code == 200
    assert response.json() == []

    # Создаем отзыв
    review = {
        "subject": "Python",
        "text": "I love Python",
        "mark": randint(0, 10),
    }
    response = requests.post("http://localhost:8000/reviews", json=review)
    assert response.status_code == 201
    review_1 = Review.model_validate(response.json())
    assert review_1.model_dump(exclude=["id"]) == review
    assert review_1.id == 1

    # Проверяю, созданный отзыв сохранился на сервере
    response = requests.get("http://localhost:8000/reviews", json=review)
    assert response.status_code == 200
    raw_reviews: list[dict[str, Any]] = response.json()
    assert isinstance(raw_reviews, list)
    assert len(raw_reviews) == 1
    raw_review = raw_reviews[0]
    review_1 = Review.model_validate(raw_review)
    assert review_1.model_dump(exclude=["id"]) == review

    # Проверяю, что отзыв можно получить по его личной ссылке
    response = requests.get("http://localhost:8000/reviews/1")
    assert response.status_code == 200
    raw_review = response.json()
    review_1 = Review.model_validate(raw_review)
    assert review_1.model_dump(exclude=["id"]) == review

    # Удаляю все отзывы 
    response = requests.delete("http://localhost:8000/reviews")
    assert response.status_code == 204
    response = requests.get("http://localhost:8000/reviews")
    assert response.status_code == 200
    assert response.json() == []

    # Проверяю, что отзыв можно получить по его личной ссылке
    response = requests.get("http://localhost:8000/reviews/1")
    assert response.status_code == 404

    # Создаем отзыв
    review = {
        "subject": "Python",
        "text": "I love Python",
        "mark": randint(0, 10),
    }
    response = requests.put("http://localhost:8000/reviews/2", json=review)
    assert response.status_code == 200
    raw_review = response.json()
    review_1 = Review.model_validate(raw_review)
    assert review_1.model_dump(exclude=["id"]) == review

     # Создаем отзыв
    review = {
        "subject": "Python",
        "text": "I have Python",
        "mark": randint(0, 10),
    }
    response = requests.put("http://localhost:8000/reviews/2", json=review)
    assert response.status_code == 200
    raw_review = response.json()
    review_1 = Review.model_validate(raw_review)
    assert review_1.model_dump(exclude=["id"]) == review

def test_invalid_create():
    # Создаем отзыв
    review = {
        "subject": "Python",
        "text": "I love Python",
        "mark": randint(0, 10),
        "x": 1,
    }
    response = requests.post("http://localhost:8000/reviews", json=review)
    debug(response.text)
    assert response.status_code == 422
