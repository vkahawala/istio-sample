from flask import Flask
from flask_restful import Resource, Api
import urllib.request as request
import json
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)


class Timing(Resource):

    @staticmethod
    @app.route("/bus_time/v1/", methods=["GET"])
    def bus_time_v1():
        bus_response = json.load(request.urlopen("http://busservice:9001/bus/"))
        # bus_response = json.load(request.urlopen("http://0.0.0.0:9001/bus/"))
        bus = bus_response['bus']
        bus_server_version = bus_response['version']

        time_response = json.load(request.urlopen("http://timeservice:9000/time/{}/".format(bus)))
        # time_response = json.load(request.urlopen("http://0.0.0.0:9000/time/{}/".format(bus)))
        time = time_response[str(bus)]
        time_server_version = time_response['version']

        return jsonify(
            {'v1': {str(bus): time, 'busServiceVersion': bus_server_version,
                    'timeServiceVersion': time_server_version}})

    @staticmethod
    @app.route("/bus_time/v2/", methods=["GET"])
    def bus_time_v2():
        bus_response = json.load(request.urlopen("http://busservice:9001/bus/"))
        # bus_response = json.load(request.urlopen("http://0.0.0.0:9001/bus/"))
        bus = bus_response['bus']
        bus_server_version = bus_response['version']

        time_response = json.load(request.urlopen("http://timeservice:9000/time/{}/".format(bus)))
        # time_response = json.load(request.urlopen("http://0.0.0.0:9000/time/{}/".format(bus)))
        time = time_response[str(bus)]
        time_server_version = time_response['version']

        return jsonify({'v2': {str(bus): time, 'busServiceVersion': bus_server_version,
                               'timeServiceVersion': time_server_version}})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999)
