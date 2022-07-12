"""Test the data loading functions"""

from tests.conftest import clubs
from server import loadClubs, loadCompetitions, get_club_by_name

def test_load_clubs_is_ok():
    """
    GIVEN a clubs.json file exists in the current directory
    WHEN loadClubs function is called
    THEN a list of 3 clubs is returned and the first club == to Simply Lift
    """
    clubs = loadClubs()
    assert len(clubs) == 3
    assert clubs[0].get('name') == "Simply Lift"
    

def test_load_competition_is_ok():
    """
    GIVEN a competitions.json file exists in the current directory
    WHEN loadCompetitions function is called
    THEN a list of 2 competitions is returned with the first competition == to Simply Lift
    """
    competitions = loadCompetitions()
    assert len(competitions) == 2
    assert competitions[0].get('name') == "Spring Festival"


def test_get_club_by_name_return_a_club(clubs):
    """
    GIVEN a Iron Temple name existing in clubs
    WHEN get_club_by_name function is called
    THEN the dictionnary of the club is returned
    """
    club = get_club_by_name(clubs, "Iron Temple")
    assert club.get('email') == "admin@irontemple.com"
    assert club.get('points') == "4"

def test_get_club_by_name_return_none(clubs):
    """
    GIVEN a club name non existing in clubs
    WHEN get_club_by_name function is called
    THEN None is returned
    """
    club = get_club_by_name(clubs, "Bad club")
    assert club is None
