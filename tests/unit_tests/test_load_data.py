"""Test the data loading functions"""

from server import loadClubs, loadCompetitions

def test_load_clubs_is_ok():
    """
    GIVEN a clubs.json file exists in the current directory
    WHEN loadClubs function is called
    THEN a list of 3 clubs is returned with the first club == to Simply Lift
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