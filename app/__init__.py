# YAMMERS
# SoftDev

from flask import Flask, render_template
app = Flask(__name__)  

@app.route("/")       
def hello_world():
    return render_template('main.html')


# redirect to game
@app.route("/game", methods=["GET","POST"])       
def game():
    return render_template('game.html')

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()