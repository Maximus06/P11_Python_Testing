import pytest

from server import clubs, get_club_by_name, update_club_points

# def test_club_points_are_correctly_updated(client):
#     """
#     GIVEN a number of points avaible for a club
#     WHEN the purchasePlaces function is called
#     THEN the club point should be correctly updated
#     """
#     competition_name = "Spring Festival"
#     club_name = "Iron Temple"

#     response = client.post('/purchasePlaces', data={
#         'competition' : competition_name,
#         'club' : club_name,
#         'places' : "4",
#         }
#     )
    
#     club = get_club_by_name(clubs, club_name)
#     assert club.get('points') == 0
    
def test_club_points_are_correctly_updated():
    """
    GIVEN a number of points to substract
    WHEN the update_club_point function is called
    THEN the remaining point should be correctly updated
    """
    start_point = 25
    point_to_substract = 12
    expected_remaining_point = 13

    result = update_club_points(start_point, point_to_substract)
    result_zero = update_club_points(start_point, 50)

    assert  result == expected_remaining_point
    assert  result_zero == 0

def test_update_club_points_raise_exception():
    """
    GIVEN points club to be string
    WHEN the update_club_point function is called
    THEN ValueError should be raise
    """

    with pytest.raises(ValueError):
        update_club_points('bad', 15)
