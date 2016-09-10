"""SF Treasures - The All-Women Hackathon San Francisco 9/10/16"""

import os
from flask import Flask, render_template, request, flash, redirect, session, jsonify
import requests
import json

app = Flask(__name__)

app.secret_key = os.environ.get('FLASK_SECRET_KEY')

app.jinja_env.undefined = StrictUndefined


###############################################################################


@app.route('/')
def show_homepage():
    """Show homepage."""

    return render_template("homepage.html")


@app.route('/game_time')
    def show_gamepage():
    """Show progress of game being played."""

    return render_template("game.html")


@app.route('/results')
    def show_winner():
    """Display winner."""

    return render_template("results.html")
    

##########################################################################

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0")
    