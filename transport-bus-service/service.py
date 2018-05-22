from flask import Flask
from flask_restful import Resource, Api
import random
from flask_jsonpify import jsonify
import os

app = Flask(__name__)
api = Api(app)


class Timing(Resource):

    @staticmethod
    @app.route("/bus/", methods=["GET"])
    def get():
        return jsonify({'bus': random.randint(1, 1000), 'version': os.environ['VERSION']})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9001)
