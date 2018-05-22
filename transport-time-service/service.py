from flask import Flask
from flask_restful import Resource, Api
from datetime import datetime
from flask_jsonpify import jsonify
import os

app = Flask(__name__)
api = Api(app)


class Timing(Resource):

    @staticmethod
    @app.route("/time/<bus_id>/", methods=["GET"])
    def get(bus_id):
        return jsonify({bus_id: datetime.now(), 'version': os.environ['VERSION']})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
