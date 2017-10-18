from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Sports, SportsPlayer

app = Flask(__name__)

engine = create_engine('sqlite:///sports.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Show all sports
@app.route('/')
@app.route('/sports/')
def showSports():
    sports = session.query(Sports).all()
    # return "This page will show all my sports"
    return render_template('sports.html', sports=sports)


# Show a sports detail with players
@app.route('/sports/<int:sports_id>/')
def showSportsDetail(sports_id):
    sports = session.query(Sports).filter_by(id=sports_id).one()
    players = session.query(SportsPlayer).filter_by(
        sports_id=sports_id).all()
    return render_template('player.html', players=players, sports=sports)



#JSON DATA
@app.route('/sports/JSON')
def sportsJSON():
    sports = session.query(Sports).all()
    return jsonify(sports=[s.serialize for s in sports])

@app.route('/sports/<int:sports_id>/player/JSON')
def sportsPlayerJSON(sports_id):
    Sports_Player = session.query(SportsPlayer).filter_by(id=sports_id).all()
    return jsonify(Sports_Player=[s.serialize for s in Sports_Player])

@app.route('/sports/<int:sports_id>/player/<int:player_id>/JSON')
def sportsPlayerIdJSON(sports_id, player_id):
    Sports_Player = session.query(SportsPlayer).filter_by(id=sports_id).one()
    return jsonify(Sports_Player=Sports_Player.serialize)

# Create a new sports
@app.route('/sports/new/', methods=['GET', 'POST'])
def newSports():
    if request.method == 'POST':
        newSports = Sports(name=request.form['name'])
        session.add(newSports)
        session.commit()
        return redirect(url_for('showSports'))
    else:
        return render_template('newSports.html')
    # return "This page will be for making a new sports"


# Edit a sports

@app.route('/sports/<int:sports_id>/edit/', methods=['GET', 'POST'])
def editSports(sports_id):
    editedSports = session.query(
        Sports).filter_by(id=sports_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedSports.name = request.form['name']
            return redirect(url_for('showSports'))
    else:
        return render_template(
            'editSports.html', sports=editedSports)

    # return 'This page will be for editing sports %s' % sports_id

# Delete a sports
@app.route('/sports/<int:sports_id>/delete/', methods=['GET', 'POST'])
def deleteSports(sports_id):
    sportsToDelete = session.query(
        Sports).filter_by(id=sports_id).one()
    if request.method == 'POST':
        session.delete(sportsToDelete)
        session.commit()
        return redirect(
            url_for('showSports', sports_id=sports_id))
    else:
        return render_template(
            'deleteSports.html', sports=sportsToDelete)
    # return 'This page will be for deleting sports %s' % sports_id




# adding a new Sports Player

@app.route(
    '/sports/<int:sports_id>/player/new/', methods=['GET', 'POST'])
def newPlayer(sports_id):
    if request.method == 'POST':
        newP = SportsPlayer(name=request.form['name'], description=request.form[
                           'description'], rank=request.form['rank'], country=request.form['country'], sports_id=sports_id)
        session.add(newP)
        session.commit()

        return redirect(url_for('showSports', sports_id=sports_id))
    else:
        return render_template('newplayer.html', sports_id=sports_id)

    return render_template('newPlayer.html', sports=sports)
    # return 'This page is for adding a new playerfor sports 
    # %sports_id


# Edit the sports player

@app.route('/sports/<int:sports_id>/player/<int:player_id>/edit',
           methods=['GET', 'POST'])
def editPlayer(sports_id, player_id):
    editedPlayer = session.query(SportsPlayer).filter_by(id=player_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedPlayer.name = request.form['name']
        if request.form['description']:
            editedPlayer.description = request.form['name']
        if request.form['rank']:
            editedPlayer.rank = request.form['rank']
        if request.form['country']:
            editedPlayer.country = request.form['country']
        session.add(editedPlayer)
        session.commit()
        return redirect(url_for('showSportsDetail', sports_id=sports_id))
    else:

        return render_template(
            'editPlayer.html', sports_id=sports_id, player_id=player_id, player=editedPlayer)

    # return 'This page is for editing the sports player %s' % player_id

# Delete the sports player


@app.route('/sports/<int:sports_id>/player/<int:player_id>/delete',
           methods=['GET', 'POST'])
def deletePlayer(sports_id, player_id):
    deletedPlayer = session.query(SportsPlayer).filter_by(id=player_id).one()
    if request.method == 'POST':
        session.delete(deletedPlayer)
        session.commit()
        return redirect(url_for('showSportsDetail', sports_id=sports_id))
    else:
        return render_template('deletePlayer.html', player=deletedPlayer)
    # return "This page is for deleting sports player %s' % player_id


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)