from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle


app = Flask(__name__)

app.config['SECRET_KEY'] = "123doggo"

debug = DebugToolbarExtension(app)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


boggle_game = Boggle()


@app.route("/", methods=["GET"])
def play_game():
    if request.method == 'GET':
            session['words'] = []
            session["score"] = 0
            boggle_game.found_words.clear()
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
    if validity == "ok":
        boggle_game.found_words.add(word)
        session["score"] =+ len(word)
    return validity
    
@app.route("/wordlist")
def word_list():
    words = list(boggle_game.found_words)
    session['words'] = list(boggle_game.found_words)
    return jsonify(words)

@app.route("/score")
def scoring():
    return jsonify(session['score'])


    


