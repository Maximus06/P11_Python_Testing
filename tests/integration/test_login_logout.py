from http import HTTPStatus


def test_login_logout(client):
    """
    GIVEN a email that exists
    WHEN the show_summary page is called
    THEN the summary page is display
    AND WHEN the logout is click
    THEN home page is display
    """

    # login    
    response = client.post('/showSummary', data={'email' : "admin@irontemple.com"})
    data = response.data.decode()

    assert response.status_code == HTTPStatus.OK
    assert data.find("<h2>Welcome, admin@irontemple.com </h2>") != -1

    # log out
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == HTTPStatus.OK
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data
