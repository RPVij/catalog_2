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
    # return "The Page will show all the sports"
    return render_template('sports.html', sports=sports)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)