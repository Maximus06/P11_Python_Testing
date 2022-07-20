"""Test the booking functions"""

from typing import Union

from server import purchasePlaces, clubs, get_club_by_name


def test_update_point(client):
    """
    GIVEN a number of points avaible for a club
    WHEN the purchasePlaces function is called
    THEN the club point should be correctly updated
    """
    competition_name = "Spring Festival"
    club_name = "Iron Temple"

    response = client.post('/purchasePlaces', data={
        'competition' : competition_name,
        'club' : club_name,
        'places' : "4",
        }
    )
    
    club = get_club_by_name(clubs, club_name)
    assert club.get('points') == 0


