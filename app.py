from flask import Flask
from flask_restful import Resource, Api
from flask import jsonify
import json


app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({'text': 'Hello World!'})


if __name__ == '__main__':
     app.run(port=5002)
