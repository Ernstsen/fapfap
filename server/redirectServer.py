from flask import Flask, redirect
from flask_cors import CORS
# noinspection PyUnresolvedReferences
from state import ServerState

app = Flask(__name__)
CORS(app)
state = ServerState()


@app.route('/')
def root():
    return redirect("https://fapfap.dk")


@app.route('/pickupline')
def pickup():
    return redirect("https://fapfap.dk/pickupline")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
