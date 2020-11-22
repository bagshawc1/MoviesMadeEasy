from flask import Flask
from flask_restful import Resource, Api
from flask import jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
  r"/*": {
    "origins": "*"
  }
})

with open('movies.json') as json_file:
    data = json.load(json_file)


@app.route("/", methods=['GET'])
def hello():
    return jsonify({'text': 'Hello World!'})


@app.route("/movies", methods=['GET'])
def get_movies():
    return data

@app.route("/recommended/<int:userId>", methods=['GET'])
def recommended(userId):
  val = {
    "1": {
     "movieId": 1,
     "title": "Toy Story (1995)",
     "genres": "Adventure|Animation|Children|Comedy|Fantasy",
           },
    "2": {
      "movieId": 2,
      "title": "Jumanji (1995)",
      "genres": "Adventure|Children|Fantasy"
    },
    "3": {
      "movieId": "3",
      "title": "Grumpier Old Men (1995)",
      "genres": "Comedy|Romance"
    },
    "4": {
      "movieId": "4",
      "title": "Waiting to Exhale (1995)",
      "genres": "Comedy|Drama|Romance"
    }
  }
  return val;


if __name__ == '__main__':
    app.run(port=5002)
