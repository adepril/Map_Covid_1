from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    html = str(date) + """
    <br>
    Server up and running !
    """
    return html

@app.route("/map")
def map():
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    html = str(date) + """
    <br>
    TODO: Carte mondiale du Covid-19
    """
    return html

if __name__ == "__main__":
    app.run()