import os
import pytest


@pytest.fixture
def client():
    from app import app

    app.testing = True
    return app.test_client()


def test_hello(client):
    response = client.get("/")
    assert response.status_code == 200
    name = os.getenv("APP_NAME", "World")
    assert f"<h3>Hello {name}!</h3>".encode() in response.data


def test_more(client):
    more = "more/of/this"
    response = client.get(f"/{more}")
    assert response.status_code == 200
    assert f"<b>Path:</b> /{more}<br/>".encode() in response.data


def test_favicon(client):
    more = "favicon.ico"
    response = client.get(f"/{more}")
    assert response.status_code == 404
