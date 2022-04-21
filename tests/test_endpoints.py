import json
from unittest.mock import patch

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

mock_joke_response = {
    "joke": "When Chuck Norris is in a crowded area, he doesn't walk around people. He walks through them."
}


def test_read_hello_word():
    response = client.get(
        "/",
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


@patch("main.requests.get")
def test_get_joke_200(mock):
    mock.return_value.status_code = 200
    mock.return_value.content = json.dumps(mock_joke_response, indent=2).encode("utf-8")
    response = client.get("/joke")
    assert response.status_code == 200
    assert response.json() == mock_joke_response


@patch("main.requests.get")
def test_get_joke_400(mock):
    mock.return_value.status_code = 400
    response = client.get("/joke")
    assert response.status_code == 400
    assert response.json() == {"error": "We have an error, try again"}
