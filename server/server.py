from flask import Flask
from flask_cors import CORS
# noinspection PyUnresolvedReferences
from state import ServerState

app = Flask(__name__)
CORS(app)
state = ServerState()


@app.route('/pickupline')
def get_pickup_line():
    line = generate_line()
    state.register(line)
    return line


@app.route('/')
def root():
    return "The service for shy people in need of a hookup"


@app.route('/status')
def status():
    return state.get_status()


def generate_line():
    return 'Dig. Mig. Spandauer.'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
