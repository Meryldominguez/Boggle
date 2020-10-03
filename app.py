from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle
import boggleApp.js

app = Flask(__name__)

app.config['SECRET_KEY'] = "123doggo"

debug = DebugToolbarExtension(app)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


boggle_game = Boggle()


@app.route("/")
def show_game():
    board = boggle_game.make_board()
    session["board"]= board
    return render_template("home.html", board=board)

@app.route("guess/<word>")
def handle_submit(word):


