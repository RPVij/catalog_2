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


# Show a sports detail
@app.route('/sports/<int:sports_id>/')
def showSportsDetail(sports_id):
    sports = session.query(Sports).filter_by(id=sports_id).one()
    items = session.query(SportsPlayer).filter_by(
        sports_id=sports_id).all()
    return render_template('player.html', items=items, sports=sports)



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







# # Delete a sports


# @app.route('/sports/<int:sports_id>/delete/', methods=['GET', 'POST'])
# def deleteSports(sports_id):
#     sportsToDelete = session.query(
#         Sports).filter_by(id=sports_id).one()
#     if request.method == 'POST':
#         session.delete(sportsToDelete)
#         session.commit()
#         return redirect(
#             url_for('showSports', sports_id=sports_id))
#     else:
#         return render_template(
#             'deleteSports.html', sports=sportsToDelete)
#     # return 'This page will be for deleting sports %s' % sports_id




# # Create a new menu item


# @app.route(
#     '/sports/<int:sports_id>/menu/new/', methods=['GET', 'POST'])
# def newMenuItem(sports_id):
#     if request.method == 'POST':
#         newItem = MenuItem(name=request.form['name'], description=request.form[
#                            'description'], rank=request.form['rank'], country=request.form['country'], sports_id=sports_id)
#         session.add(newItem)
#         session.commit()

#         return redirect(url_for('showMenu', sports_id=sports_id))
#     else:
#         return render_template('newmenuitem.html', sports_id=sports_id)

#     return render_template('newMenuItem.html', sports=sports)
#     # return 'This page is for making a new menu item for sports %s'
#     # %sports_id

# # Edit a menu item


# @app.route('/sports/<int:sports_id>/menu/<int:menu_id>/edit',
#            methods=['GET', 'POST'])
# def editMenuItem(sports_id, menu_id):
#     editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
#     if request.method == 'POST':
#         if request.form['name']:
#             editedItem.name = request.form['name']
#         if request.form['description']:
#             editedItem.description = request.form['name']
#         if request.form['rank']:
#             editedItem.rank = request.form['rank']
#         if request.form['country']:
#             editedItem.country = request.form['country']
#         session.add(editedItem)
#         session.commit()
#         return redirect(url_for('showMenu', sports_id=sports_id))
#     else:

#         return render_template(
#             'editmenuitem.html', sports_id=sports_id, menu_id=menu_id, item=editedItem)

#     # return 'This page is for editing menu item %s' % menu_id

# # Delete a menu item


# @app.route('/sports/<int:sports_id>/menu/<int:menu_id>/delete',
#            methods=['GET', 'POST'])
# def deleteMenuItem(sports_id, menu_id):
#     itemToDelete = session.query(MenuItem).filter_by(id=menu_id).one()
#     if request.method == 'POST':
#         session.delete(itemToDelete)
#         session.commit()
#         return redirect(url_for('showMenu', sports_id=sports_id))
#     else:
#         return render_template('deleteMenuItem.html', item=itemToDelete)
#     # return "This page is for deleting menu item %s" % menu_id


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)