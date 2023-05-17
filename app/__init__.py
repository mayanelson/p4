# YAMMERS
# SoftDev
import db_tools
from flask import Flask, render_template
app = Flask(__name__)  
@app.route("/")       
def hello_world():
    return render_template('main.html')

# redirect to game
@app.route("/game", methods=["GET","POST"])       
def game():
    data = db_tools.get_random_data()
    boro_data = db_tools.get_random_boros(data[1:])
    print(boro_data)
    boro_keys = list(boro_data)
    converted_name = db_tools.convert_name(data[0])
    return render_template('game.html', db_name=converted_name, boro_data=list(boro_data.values()), boro_keys=boro_keys)

# redirect to map
@app.route("/map", methods=["GET","POST"])       
def map():
    return render_template('map.html')

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()