import json
import sys
from flask import Flask, jsonify, Response

#heuristic: hands on, not abstract

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to pioTracker netScrape!"

#detect timeout of browser process and reload it!
@app.route('/api/v1/all', methods=['GET'])
def getBusList():
	f = open("locations.txt", "r")
	response = f.read();
	f.close()

	return Response(response, mimetype='application/json')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False, port=80)
