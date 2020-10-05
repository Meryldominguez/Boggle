from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle


app = Flask(__name__)

app.config['SECRET_KEY'] = "123doggo"

debug = DebugToolbarExtension(app)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


boggle_game = Boggle()
good_words=[]


@app.route("/", methods=["GET"])
def play_game():
    if request.method == 'GET':
            board = boggle_game.make_board()
            session["board"]= board
            return render_template("home.html", board=board)
    # if request.method == 'POST':
    #     word = request.form['word']
    #     board= session["board"]
    #     valid = boggle_game.check_valid_word(board,word)
    #     if valid == "ok":
    #         good_words.append(word)
    #         return render_template("home.html", words=good_words, board=board)

@app.route("/check-word", methods=["POST"])
def check_word():
    post = request.get_json()
    word = post['word']
    board= session["board"]
    validity = boggle_game.check_valid_word(board,word)
    return validity
    
# @app.route("/wordcheck")
# def word_check():
#     word = request.args.get("word")
#     return redirect("/")


    


