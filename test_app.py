import requests


def test_root():
    response = requests.get("http://localhost:8000/")
    assert response.status_code == 200
    assert response.json() == "hello world"


def test_languages():
    response = requests.get("http://localhost:8000/languages")
    assert response.status_code == 200
    assert response.json() == {"jana": "python"}
