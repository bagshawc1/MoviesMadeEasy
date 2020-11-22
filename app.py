from __future__ import print_function # In python 2.7
from flask import Flask
from flask_restful import Resource, Api
from flask import jsonify
from flask_cors import CORS
import json
import pickle
model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
  r"/*": {
    "origins": "*"
  }
})

with open('movies.json') as json_file:
    data = json.load(json_file)
    for p in data:
        print(data[p]['title'])


@app.route("/", methods=['GET'])
def hello():
    return jsonify({'text': 'Hello World!'})


@app.route("/movies", methods=['GET'])
def get_movies():
    return data


if __name__ == '__main__':
    app.run(port=5002)
