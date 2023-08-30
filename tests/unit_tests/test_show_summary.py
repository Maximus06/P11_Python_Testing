from http import HTTPStatus
import pytest

# from tests.conftest import client

from server import EmailNotFound, show_summary, get_club
import server


# def test_should_status_code_ok(client):
# 	response = client.get('/index')
# 	assert response.status_code == 200


def test_get_club_with_email_existing():
    """
    GIVEN a email that exists
    WHEN the get_club function is called
    THEN the club is return

    ARRANGE
    ACT
    ASSERT
    """
    # Given / Arrange
    email = "admin@irontemple.com"

    # When / Act
    club = get_club(email)

    expected_value = "Iron Temple"
    # Then / assert
    assert club.get("name") == expected_value


def test_get_club_with_email_not_existing():
    """
    GIVEN a email that does not exist
    WHEN the get_club function is called
    THEN the EmailNotFound exception is raise
    """
    with pytest.raises(EmailNotFound):
        get_club("bademail@gmail.com")


def test_show_summary_ok(client, monkeypatch, mocker, competitions):
    """
    GIVEN a email that exists
    WHEN the show_summary page is called
    THEN the summary page is display
    """

    # avec monkeypatch
    def patch_get_club(dummy):
        """Mock the get_club function"""
        return {"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"}

    monkeypatch.setattr(server, "get_club", patch_get_club)

    # avec mocker
    # club = {"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"}
    # mocker.patch("server.get_club", return_value=club)

    monkeypatch.setattr(server, "competitions", competitions)
    # avec mocker
    # mocker.patch.object(server, "competitions", competitions)

    response = client.post("/showSummary", data={"email": "admin@irontemple.com"})
    data = response.data.decode()

    assert response.status_code == HTTPStatus.OK
    assert data.find("<h2>Welcome, admin@irontemple.com </h2>") != -1


def test_not_allowed_with_get(client):
    """
    GET method is not allowed
    """

    response = client.get("/showSummary")

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
