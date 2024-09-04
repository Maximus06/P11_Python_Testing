import pytest

import server
from server import (
    valid_booking,
    MaxBookingLimitError,
    NotEnoughtPoint,
    NotEnoughtPendingPlace,
    ExpiredCompetition,
)


def test_purchase_place_is_ok(client, mocker, clubs, competitions):
    mocker.patch.object(server, "clubs", clubs)
    mocker.patch.object(server, "competitions", competitions)

    response = client.post(
        "/purchasePlaces",
        data={"competition": "Spring Festival", "club": "Simply Lift", "places": "5"},
        follow_redirects=True,
    )

    assert b"Great-booking complete!" in response.data


def test_valid_booking_return_true():
    """
    GIVEN valid parameters
    WHEN the valid_booking fonction is called
    THEN valid_booking return True
    """
    result = valid_booking(place_required=12, club_place=15, pending_place=20)
    assert result is True


def test_valid_booking_raise_ValueError():
    """
    GIVEN a bad value for the place required (e.g: a letter or a negative number)
    WHEN the valid_booking fonction is called
    THEN ValueError should be raise
    """
    with pytest.raises(ValueError):
        valid_booking(place_required="a", club_place=15, pending_place=20)

    with pytest.raises(ValueError):
        valid_booking(place_required=-5, club_place=15, pending_place=20)


def test_valid_booking_raise_MaxBookingLimitError():
    """
    GIVEN a number of place required > to the maximum allowed
    WHEN the valid_booking fonction is called
    THEN MaxBookingLimitError should be raise
    """
    with pytest.raises(MaxBookingLimitError):
        valid_booking(place_required=13, club_place=15, pending_place=20)


def test_valid_booking_raise_NotEnoughtPoint():
    """
    GIVEN a number of place required > to the club point
    WHEN the valid_booking fonction is called
    THEN NotEnoughtPoint should be raise
    """
    with pytest.raises(NotEnoughtPoint):
        valid_booking(place_required=10, club_place=8, pending_place=20)


def test_valid_booking_raise_NotEnoughtPendingPlace():
    """
    GIVEN a number of place required > to competition pending place
    WHEN the valid_booking fonction is called
    THEN NotEnoughtPendingPlace should be raise
    """
    with pytest.raises(NotEnoughtPendingPlace):
        valid_booking(place_required=10, club_place=15, pending_place=8)


# def test_valid_booking_raise_ExpiredCompetition():
#     """
#     GIVEN a booking for a ....
#     WHEN the valid_booking fonction is called
#     THEN NotEnoughtPendingPlace should be raise
#     """
#     with pytest.raises(ExpiredCompetition):
#         valid_booking(place_required=10, club_place=15, pending_place=8)
