from flask import Flask, render_template, redirect, url_for, session, request
import random
from games import pingpong, chess, ludo

app = Flask(__name__)
app.secret_key = "supersecretkey"

GAMES = {
    "pingpong": pingpong,
    "chess": chess,
    "ludo": ludo,
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/surprise")
def surprise():
    game = random.choice(list(GAMES.keys()))
    session['surprise_rule'] = True
    return redirect(url_for(game))

@app.route("/pingpong", methods=["GET", "POST"])
def pingpong():
    return pingpong.handle_game(request, session)

@app.route("/chess", methods=["GET", "POST"])
def chess():
    return chess.handle_game(request, session)

@app.route("/ludo", methods=["GET", "POST"])
def ludo():
    return ludo.handle_game(request, session)

if __name__ == "__main__":
    app.run(debug=True)