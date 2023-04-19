import pytest
from server import app as server_app



@pytest.fixture
def app():
    server_app.config.from_mapping({'TESTING': True})
    yield server_app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()

@pytest.fixture
def clubs():
    return [
        {
            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "13"
        },
        {
            "name": "Iron Temple",
            "email": "admin@irontemple.com",
            "points": "4"
        },
        {   "name": "She Lifts",
            "email": "kate@shelifts.co.uk",
            "points": "12"
        }
    ]

@pytest.fixture
def competitions():
    return [
        {
            "name": "Spring Festival",
            "date": "2024-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        },
        {
            "name": "Arnold Classic",
            "date": "2024-04-04 13:00:00",
            "numberOfPlaces": "15"
        }
    ]