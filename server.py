import json
from flask import Flask, render_template, request, redirect, flash, url_for
from datetime import datetime


MAX_PLACES_PER_COMPETITION = 12


def loadClubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions


def validate_club_points(club, places_required):
    """Check if club has enough points to purchase places."""
    if places_required > int(club['points']):
        raise ValueError("Not enough points available.")
    return True


def validate_max_places(places_required):
    """Ensure requested places does not exceed the allowed maximum."""
    if places_required > MAX_PLACES_PER_COMPETITION:
        raise ValueError(
            f"Cannot book more than {MAX_PLACES_PER_COMPETITION} places."
            )
    return True


def validate_competition_overbooking(competition, places_required):
    """Ensure that requested places don't exceed competition availability."""
    if places_required > int(competition['numberOfPlaces']):
        raise ValueError("Not enough places available in the competition.")
    return True


def validate_competition_date(competition_date, current_date=None):
    if current_date is None:
        current_date = datetime.now()

    competition_date = datetime.strptime(competition_date, "%Y-%m-%d %H:%M:%S")
    if competition_date < current_date:
        raise ValueError("The competition date has passed.")
    return True


def update_club_points(club, places_required):
    club['points'] = str(int(club['points']) - places_required)
    return club['points']


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def showSummary():
    email = request.form['email']
    try:
        club = [club for club in clubs if club['email'] == email][0]
        return render_template(
            'welcome.html',
            club=club,
            competitions=competitions
        )
    except IndexError:
        flash("Sorry, that email wasn't found.")
        return render_template('index.html'), 404


@app.route('/book/<competition>/<club>')
def book(competition, club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        try:
            validate_competition_date(
                competition_date=foundCompetition['date']
            )
            return render_template(
                'booking.html',
                club=foundClub,
                competition=foundCompetition
            )
        except ValueError as error_message:
            flash(str(error_message))
            return render_template(
                'welcome.html',
                club=foundClub,
                competitions=competitions
            )
    else:
        flash("Something went wrong-please try again")
        return render_template(
            'welcome.html',
            club=club,
            competitions=competitions
        )


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition = [
        c for c in competitions if c['name'] == request.form['competition']
    ][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])

    # Validate and process the purchase
    try:
        validate_competition_overbooking(
            competition=competition,
            places_required=placesRequired
        )
        validate_club_points(club=club, places_required=placesRequired)
        validate_max_places(places_required=placesRequired)
        competition['numberOfPlaces'] = (
            int(competition['numberOfPlaces'])-placesRequired
        )
        club['points'] = update_club_points(
            club=club,
            places_required=placesRequired
        )
        flash('Great-booking complete!')
        return render_template(
            'welcome.html',
            club=club, competitions=competitions
        )
    except ValueError as error_message:
        flash(str(error_message))
        return render_template(
            'booking.html',
            club=club,
            competition=competition
        ), 400


@app.route("/pointsBoard")
def pointsBoard():
    return render_template('points_board.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
