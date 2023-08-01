from http import HTTPStatus
import pytest

import server


def test_show_summary_with_good_email(client):
    """
    GIVEN a email that exists
    WHEN the show_summary page is called
    TH# There is no `E` mentioned in the provided code, so it is unclear what `E` is referring to.
    EN the summary page is display"""

    response = client.post("/showSummary", data={"email": "admin@irontemple.com"})
    data = response.data.decode()

    assert response.status_code == HTTPStatus.OK
    assert data.find("<h2>Welcome, admin@irontemple.com </h2>") != -1


def test_show_summary_with_email_not_existing(client):
    """
    GIVEN a email that not exists
    WHEN the show_summary page is called
    THEN the summary page is display with a error message"""

    bademail = "bademail@irontemple.com"
    response = client.post(
        "/showSummary", data={"email": "bademail@irontemple.com"}, follow_redirects=True
    )

    data = response.data.decode()

    expected_error = f"Error: email {bademail} does not exist. Please try again."
    # assert response.status_code == HTTPStatus.OK
    # assert data.find("Error") != -1
    assert expected_error in data
