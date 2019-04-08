from flask import Flask, redirect
from flask_cors import CORS
# noinspection PyUnresolvedReferences
from state import ServerState

app = Flask(__name__)
CORS(app)
state = ServerState()

baseUrl= "fapfap.e-software.dk"

@app.route('/')
def root():
    return redirect("https://" + baseUrl)


@app.route('/pickupline')
def pickup():
    return redirect("https://" + baseUrl + "/pickupline")

@app.route('/status')
def status():
    return redirect("https://" + baseUrl + "/pickupline")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
