from flask import Flask, request, render_template, redirect, flash, session, jsonify
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
<<<<<<< Updated upstream
=======
            session['words'] = []
            session["score"] = 0
            boggle_game.found_words.clear()
>>>>>>> Stashed changes
            board = boggle_game.make_board()
            session["board"]= board
            return render_template("home.html", board=board)

@app.route("/check-word", methods=["POST"])
def check_word():
    post = request.get_json()
    word = post['word']
    board= session["board"]
    validity = boggle_game.check_valid_word(board,word)
<<<<<<< Updated upstream
    print(validity)
=======
    if validity == "ok":
        boggle_game.found_words.add(word)
        session["score"] =+ len(word)
>>>>>>> Stashed changes
    return validity
    
# @app.route("/wordcheck")
# def word_check():
#     word = request.args.get("word")
#     return redirect("/")

@app.route("/score")
def scoring():
    return jsonify(session['score'])


    


