import requests
from devtools import debug
from random import randint

def test_root():
    response = requests.get("http://localhost:8000/")
    assert response.status_code == 200
    assert response.json() == "hello world"


def test_languages():
    response = requests.get("http://localhost:8000/languages")
    assert response.status_code == 200
    assert response.json() == {"jana": "python"}


def test_reviews():
    # Проверяю, что сначала отзывов нет
    response = requests.get("http://localhost:8000/reviews")
    assert response.status_code == 200
    assert response.json() == []

    # Создаем отзыв
    review = {'subject': 'Python', 'text': 'I love Python', 'mark': randint(0, 10)}
    response = requests.post("http://localhost:8000/reviews", json=review)
    debug(response.headers)
    assert response.status_code == 201
    assert response.json() == review
