from __future__ import print_function # In python 2.7
from flask import Flask
from flask_restful import Resource, Api
from flask import jsonify
from flask import make_response
from flask import abort
import sys
import logging
#.pth

app = Flask(__name__)
api = Api(app)


users = [
    {
        'id': 1,
        'title': u'Toy Story',
        'description': u'Recommend 5 stars', 
    },
    {
        'id': 2,
        'title': u'Shrek',
        'description': u'2 stars', 
    }
] 

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

#user id, movie title , rating
@app.route("/") #main route
def hello():
    return jsonify({'text': 'Hello World!'})



@app.route('/users', methods =['GET'])  ## get to return entire json
def get_users():
    return jsonify({'users': users})

@app.route('/users/<int:user_id>', methods =['GET']) #get a specific user
def get_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    logging.debug(jsonify({'user': user[0]}))
    if len(user) == 0:
        abort(404)
    return jsonify({'user': user[0]})




# class User(Resource):
#     def get(self, user_id):
#         print('User_ID:' + user_id)
#        # result = {'data': {'id': data.id}}
#       #  return jsonify(result)

# api.add_resource(User, '/user/<user_id>')  #First route



class Movies(Resource):
    def get(self):
        return{'movies': [{'title': 'Toy Story', 'date': 'march'}]}

api.add_resource(Movies, '/movie')









if __name__ == '__main__':
     app.run(port=5002)
