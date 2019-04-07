import argparse

from flask import Flask
from flask_cors import CORS
# noinspection PyUnresolvedReferences
from predictor import Predictor
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
    predictor = Predictor.getInstance("fapping_model/models/model.h5", "fapping_model/models/tokenizer.pkl")
    return predictor.predict()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate_path")
    parser.add_argument("private_key_path")
    args = parser.parse_args()

    app.run(host='0.0.0.0', port=443, ssl_context=(args.certificate_path,
                                                   args.private_key_path))
