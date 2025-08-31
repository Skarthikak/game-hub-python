from flask import render_template
import random

def handle_game(request, session):
    # Unique logic: show wild squares with random effects
    wild_squares = random.sample(["A1", "C3", "E5", "G7"], k=2)
    effects = ["extra_move", "piece_swap"]
    context = {
        "wild_squares": wild_squares,
        "effects": effects,
        "surprise": session.get('surprise_rule', False)
    }
    return render_template("chess.html", **context)