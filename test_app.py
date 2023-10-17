import requests
from devtools import debug
from random import randint
import pytest


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
    assert response.json() == review

     # Проверяю, созданный отзыв сохранился на сервере
    response = requests.get("http://localhost:8000/reviews")
    assert response.status_code == 200
    assert response.json() == [review]

    # Удаляю все отзывы 
    response = requests.delete("http://localhost:8000/reviews")
    assert response.status_code == 204
    response = requests.get("http://localhost:8000/reviews")
    assert response.status_code == 200
    assert response.json() == []


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
