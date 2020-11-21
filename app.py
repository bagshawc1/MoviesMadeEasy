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
