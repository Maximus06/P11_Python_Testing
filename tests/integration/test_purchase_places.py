"""Test the booking functions"""

from typing import Union

from server import clubs, get_club_by_name


def test_update_point_with_enought_point(client):
    """
    GIVEN a number of points avaible for a club
    WHEN the purchasePlaces function is called
    THEN the club point should be correctly updated
    """
    competition_name = "Spring Festival"
    club_name = "Iron Temple"
    club_point_expected = 0

    response = client.post(
        "/purchasePlaces",
        data={
            "competition": competition_name,
            "club": club_name,
            "places": "4",
        },
    )

    club = get_club_by_name(clubs, club_name)

    assert int(club.get("points")) == club_point_expected
