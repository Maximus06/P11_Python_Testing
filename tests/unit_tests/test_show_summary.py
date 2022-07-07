import pytest
from tests.conftest import client

from server import EmailNotFound, show_summary, get_club


# def test_should_status_code_ok(client):
# 	response = client.get('/index')
# 	assert response.status_code == 200


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'    

def test_get_club_with_email_existing():
    """
    GIVEN a email that exists
    WHEN the get_club function is called
    THEN the club is return
    """
    club = get_club("admin@irontemple.com")
    assert club.get('name') == "Iron Temple"


def test_get_club_with_email_not_existing():
    """
    GIVEN a email that does not exist
    WHEN the get_club function is called
    THEN the EmailNotFound exception is raise
    """
    with pytest.raises(EmailNotFound):
        get_club("bademail@gmail.com")


def test_show_summary_ok(client):
    """
    GIVEN a email that exists
    WHEN the show_summary is called
    THEN the summary page is display
    """    

    # with pytest.raises(ValueError):
    #     client.post('/showSummary', data={'email' : "admin@irontemple.com"})
    
    response = client.post('/showSummary', data={'email' : "admin@irontemple.com"})
    data = response.data.decode()

    assert response.status_code == 200
    assert data.find("<h2>Welcome, admin@irontemple.com </h2>") != -1
       