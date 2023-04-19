"""Test the data loading functions"""

from server import loadClubs, loadCompetitions, get_club_by_name, get_competition_by_name

def test_load_clubs_is_ok():
    """
    GIVEN a clubs.json file existing in the current directory with known data
    WHEN loadClubs function is called
    THEN a list of 3 clubs is returned and the first club is "Simply Lift"

    AAA
    Arrange
    ACT
    Assert
    """
    name_expected = "Simply Lift"

    clubs = loadClubs()

    assert len(clubs) == 3
    assert clubs[0].get('name') == "Simply Lift"
    

def test_load_competition_is_ok():
    """
    GIVEN a competitions.json file with known data existing in the current directory
    WHEN loadCompetitions function is called
    THEN a list of 2 competitions is returned with the first competition == "Spring Festival"
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
    club_name = "Iron Temple"
    expected_email = "admin@irontemple.com"
    expected_point = "4"

    club = get_club_by_name(clubs, club_name)

    assert club.get('email') == expected_email
    assert club.get('points') == expected_point

def test_get_club_by_name_return_none(clubs):
    """
    GIVEN a club name non existing in clubs
    WHEN get_club_by_name function is called
    THEN None is returned
    """
    club = get_club_by_name(clubs, "Bad club")
    assert club is None

def test_get_competition_by_name_return_a_competition(competitions):
    """
    GIVEN a arnold classic name existing in competition
    WHEN get_competition_by_name function is called
    THEN the dictionnary of the competition is returned
    """
    expected_name = "Arnold Classic"
    expected_place = "15"

    competition = get_competition_by_name(competitions, expected_name)

    assert competition.get('name') == expected_name
    assert competition.get('numberOfPlaces') == expected_place

def test_get_competition_by_name_return_none(competitions):
    """
    GIVEN a competition name not existing in competitions
    WHEN get_competition_by_name function is called
    THEN None is returned
    """
    expected_name = "Bad name"

    competition = get_competition_by_name(competitions, expected_name)

    assert competition is None
    