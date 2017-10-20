from flask import Flask, flash, render_template, request, redirect, jsonify, \
    url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random
import string

from urllib3.connectionpool import xrange

from database_setup import Base, User, Sports, SportsPlayer
from flask import make_response
import requests
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json

from flask import session as login_session

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secret.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Sports Player Application"

# Connecting to a database
engine = create_engine('sqlite:///sports.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Show all sports
@app.route('/')
@app.route('/sports/')
def showSports():
    print(login_session)
    sports = session.query(Sports).all()
    # return "This page will show all my sports"
    return render_template('sports.html', sports=sports,
                           login_session=login_session)


# Show a sports detail with players
@app.route('/sports/<int:sports_id>/')
def showSportsDetail(sports_id):
    sports = session.query(Sports).filter_by(id=sports_id).one()
    players = session.query(SportsPlayer).filter_by(
        sports_id=sports_id).all()
    return render_template('player.html', players=players, sports=sports,
                           login_session=login_session)


# JSON DATA
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
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newSports = Sports(name=request.form['name'],
                           user_id=login_session['user_id'])
        session.add(newSports)
        flash('New Sports %s Successfully Created' % newSports.name)
        session.commit()
        return redirect(url_for('showSports'))
    else:
        return render_template('newSports.html', login_session=login_session)
        # return "This page will be for making a new sports"


# Edit a sports

@app.route('/sports/<int:sports_id>/edit/', methods=['GET', 'POST'])
def editSports(sports_id):
    editedSports = session.query(
        Sports).filter_by(id=sports_id).one()
    if 'username' not in login_session:
        return redirect('/login')
        if editedSports.user_id != login_session['user_id']:
            return "<script>function myFunction() {alert('You \
            are not authorized to edit this sports.\
             Please create your own sports in order \
             to edit.');}</script><body onload='myFunction()'>"
    if request.method == 'POST':
        if request.form['name']:
            editedSports.name = request.form['name']
            return redirect(url_for('showSports'))
    else:
        return render_template(
            'editSports.html', sports=editedSports,
            login_session=login_session)

    # return 'This page will be for editing sports %s' % sports_id

# Delete a sports


@app.route('/sports/<int:sports_id>/delete/', methods=['GET', 'POST'])
def deleteSports(sports_id):
    sportsToDelete = session.query(
        Sports).filter_by(id=sports_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if sportsToDelete.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You\
         are not authorized to delete this Sports.\
          Please create your own sports in order\
           to delete.');}</script><body onload='myFunction()'>"
    if request.method == 'POST':
        session.delete(sportsToDelete)
        session.commit()
        return redirect(
            url_for('showSports', sports_id=sports_id))
    else:
        return render_template(
            'deleteSports.html', sports=sportsToDelete,
            login_session=login_session)
    # return 'This page will be for deleting sports %s' % sports_id


# adding a new Sports Player

@app.route(
    '/sports/<int:sports_id>/player/new/', methods=['GET', 'POST'])
def newPlayer(sports_id):
    sports = session.query(Sports).filter_by(id=sports_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newP = SportsPlayer(name=request.form['name'],
                            description=request.form[
            'description'], rank=request.form['rank'],
            country=request.form['country'], sports_id=sports_id,
            user_id=sports.user_id)
        session.add(newP)
        session.commit()
        flash('New Sports Player: %s . Successfully Created' % (newP.name))
        return redirect(url_for('showSports', sports_id=sports_id))
    else:
        return render_template('newplayer.html', sports_id=sports_id)

    return render_template('newPlayer.html', sports_id=sports_id,
                           login_session=login_session)
    # return 'This page is for adding a new playerfor sports
    # %sports_id


# Edit the sports player

@app.route('/sports/<int:sports_id>/player/<int:player_id>/edit',
           methods=['GET', 'POST'])
def editPlayer(sports_id, player_id):
    editedPlayer = session.query(SportsPlayer).filter_by(id=player_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if login_session['user_id'] != editedPlayer.user_id:
        return "<script>function myFunction() {alert('You \
        are not authorized to edit player to this sports.\
         Please create your own Sports in order to edit \
         Players.');}</script><body onload='myFunction()'>"
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
        return redirect(url_for('showSportsDetail',
                                sports_id=sports_id,
                                login_session=login_session))
    else:

        return render_template(
            'editPlayer.html', sports_id=sports_id, player_id=player_id,
            player=editedPlayer, login_session=login_session)

        # return 'This page is for editing the sports player %s' % player_id


# Delete the sports player


@app.route('/sports/<int:sports_id>/player/<int:player_id>/delete',
           methods=['GET', 'POST'])
def deletePlayer(sports_id, player_id):
    deletedPlayer = session.query(SportsPlayer).filter_by(id=player_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if login_session['user_id'] != deletedPlayer.user_id:
        return "<script>function myFunction() {alert('You \
        are not authorized to delete player to this \
        sports. ');}</script><body onload='myFunction()'>"
    if request.method == 'POST':
        session.delete(deletedPlayer)
        session.commit()
        return redirect(url_for('showSportsDetail',
                                sports_id=sports_id),
                        login_session=login_session)
    else:
        return render_template('deletePlayer.html',
                               player=deletedPlayer,
                               login_session=login_session)
        # return "This page is for deleting sports player %s' % player_id

        # Auth views

        # the below code snippet function is from
        # https://github.com/udacity/ud330/blob/master/Lesson2/step5/project.py


# Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secret.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print("Token's client ID does not match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps('Current user is already connected.'),
            200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    user_id = getUserID(data['email'])
    print(user_id)
    if not user_id:
        add_user = createUser(login_session)
        login_session['user_id'] = add_user

    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px;\
     height: 300px;border-radius: 150px;\
     -webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print("done!")
    return output


# User Helper Functions


def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
        'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


# DISCONNECT - Revoke a current user's token and reset their login_session
 # he below code snippet function is from
 # https://github.com/udacity/ud330/blob/master/Lesson2/step5/project.py

@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print('Access Token is None')
        response = make_response(json.dumps('Current user not connected.'),
                                 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print('In gdisconnect access token is %s', access_token)
    print('User name is: ')
    print(login_session['username'])
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % \
          login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print('result is ')
    print(result)
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return redirect(url_for('showSports'))
    else:
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


if __name__ == '__main__':
    app.secret_key = 'my_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
