from flask import render_template
import random

def handle_game(request, session):
    # Unique logic: dice can trigger mini-games
    dice = random.randint(1, 6)
    mini_game = random.choice(["reaction", "puzzle", "memory"]) if dice == 6 else None
    context = {
        "dice": dice,
        "mini_game": mini_game,
        "surprise": session.get('surprise_rule', False)
    }
    return render_template("ludo.html", **context)
