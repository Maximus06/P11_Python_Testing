import json

from flask import Flask, render_template, request, redirect, flash, url_for

# Maximum booking place allowed
MAX_BOOKING = 12

class EmailNotFound(Exception):
    pass

def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


def get_club_by_name(clubs: list, club_name: str) -> dict | None:
    """Return the first club matching the name or None"""
    for club in clubs:
        if club.get('name') == club_name:
            return club
    return None

def get_competition_by_name(competitions: list, competition_name: str) -> dict | None:
    """Return the first competition matching the name or None"""
    for compet in competitions:
        if compet.get('name') == competition_name:
            return compet
    return None

def update_club_points(club_point: str, point_to_substract: int) -> int:
    """Return the updated point of a club after booking"""
    try:
        updated_point =  int(club_point) - point_to_substract
    except ValueError:
        error_msg = f"Une erreur est survenue dans la fonction update_club_points car les points des clubs ne sont pas des entiers"
        raise ValueError(error_msg)
    
    if updated_point < 0:
        updated_point = 0

    return updated_point


def get_club(email: str) -> dict:
    """Return the first club matching the email"""
    for club in clubs:
        if email == club.get('email'):
            return club
    raise EmailNotFound


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def show_summary():
    """Render the available competitions"""

    # club = [club for club in clubs if club['email'] == request.form['email']][0]
        
    try:
        club = get_club(request.form['email'])
    except EmailNotFound:
        flash(f"Error: email {request.form['email']} does not exist. Please try again.")
        return redirect(url_for('index'))
    
    return render_template('welcome.html',club=club,competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition,club):
    """Render the booking page"""
    # foundClub = [c for c in clubs if c['name'] == club][0]
    found_club = get_club_by_name(clubs, club_name=club)

    # foundCompetition = [c for c in competitions if c['name'] == competition][0]
    found_competition = get_competition_by_name(competitions, competition_name=competition)

    if found_club and found_competition:
        return render_template('booking.html',club=found_club,competition=found_competition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    # récupére la compétition
    # competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    competition = get_competition_by_name(competitions, request.form['competition'])

    # Récupére le club
    # club = [c for c in clubs if c['name'] == request.form['club']][0]
    club = get_club_by_name(clubs, request.form['club'])

    placesRequired = int(request.form['places'])

    # valid max booking < 12 and club point > place required and competion date < date today

    # Mise à jour des places restantes pour la compétition
    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired

    # update the club points
    club['points'] = update_club_points(int(club['points']), placesRequired) 
    # club['points'] = int(club['points']) - placesRequired

    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))