from flask import render_template

def handle_game(request, session):
    # Unique logic: random obstacles + power-ups shown in template
    powerups = ["Slow Ball", "Multi-Ball", "Shrink Paddle"]
    obstacles = ["Wall", "Bumper", "Hole"]
    context = {
        "powerups": powerups,
        "obstacles": obstacles,
        "surprise": session.get('surprise_rule', False)
    }
    return render_template("pingpong.html", **context)