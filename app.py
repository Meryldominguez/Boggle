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
    if not session.get('plays'):
        session['plays'] = 1
    elif session.get('plays'):
        session['plays']= session['plays']+1
    if not session.get('high_score'):
        session['high_score']= 0
    boggle_game.found_words.clear()
    board = boggle_game.make_board()
    session["board"]= board
    return render_template("home.html", board=board, plays = session['plays'], high_score=session['high_score'])

@app.route("/check-word", methods=["POST"])
def check_word():
    post = request.get_json()
    word = post['word']
    board= session["board"]
    validity = boggle_game.check_valid_word(board,word)
    if validity == "ok":
        boggle_game.found_words.add(word)
        boggle_game.score = boggle_game.score + len(word)
    return validity
    
@app.route("/wordlist")
def word_list():
    words = list(boggle_game.found_words)
    session['words'] = list(boggle_game.found_words)
    return jsonify(words)

@app.route("/score",methods=["GET","POST"])
def scoring():
    if request.method == 'POST':
        post = request.get_json()
        print(post)
        curr_score = int(post["score"])
        high_score = session["high_score"]
        if curr_score> high_score:
            session['high_score'] = curr_score
        return post
        
    else:
        return jsonify(boggle_game.score)


    


