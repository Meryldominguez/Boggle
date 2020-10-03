from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle


app = Flask(__name__)

app.config['SECRET_KEY'] = "123doggo"

debug = DebugToolbarExtension(app)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


boggle_game = Boggle()


@app.route("/", methods=["GET","POST"])
def play_game():
    if request.method == 'GET':
        """return the information for <user_id>"""
        if session["board"]:
            return render_template("home.html", board=session["board"])
        else:
            board = boggle_game.make_board()
            session["board"]= board
            return render_template("home.html", board=board)
    if request.method == 'POST':
        word = request.form['word']
        print(word)
        return render_template("home.html", board = session["board"])
    
# @app.route("/wordcheck")
# def word_check():
#     word = request.args.get("word")
#     return redirect("/")


    


