from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pingpong')
def pingpong():
    return render_template('pingpong.html')

@app.route('/chess')
def chess():
    return render_template('chess.html')

@app.route('/ludo')
def ludo():
    return render_template('ludo.html')

if __name__ == '__main__':
    app.run(debug=True)