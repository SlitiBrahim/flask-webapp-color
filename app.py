import os
from flask import Flask
from flask import render_template
import socket
import os

app = Flask(__name__)

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}

color = 'green'

@app.route("/")
def main():
    print(color)
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[color])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
