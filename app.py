# from __future__ import print_function # In python 2.7
from flask import Flask
from flask_restful import Resource, Api
from flask import jsonify
from flask_cors import CORS
import json
import pickle
import time

from fastai.tabular.all import *
from fastai.collab import *

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
  path = Path('Hack-Western-7/ml-latest-small')
  model_path = Path('Hack-Western-7/models')

  ratings = pd.read_csv(path/'ratings.csv')
  movies = pd.read_csv(path/'movies.csv')

  ratings = ratings.merge(movies)
  ratings = ratings[["userId", "title", "rating"]]

  data_collab = CollabDataLoaders.from_df(ratings, item_name='title', bs=5)

  learn = collab_learner(data_collab, n_factors=50, y_range=(0, 5.5))
  loaded_learner = learn.load('model-1')

  dls = CollabDataLoaders.from_df(ratings, item_name='title', bs=64)

  userId = 2
  rows = []
  rating_ind = 0

  user_watched = ratings[ratings["userId"] == userId]
  user_watched_titles = user_watched.loc[:, "title"]
  movie_list = np.unique(ratings[['title']])

  new_movies = np.setdiff1d(movie_list, user_watched_titles)

  for i in range(len(new_movies)):
      rows.append(dict({'userId': userId, 'title': new_movies[i], 'rating': rating_ind}))
      rating_ind += 1

  test_data = pd.DataFrame(rows)

  test_collab = CollabDataLoaders.from_df(test_data, item_name='title', shuffle_train=False, bs=64, valid_pct=0.0, seed=42)

  preds, targs = loaded_learner.get_preds(dl=test_collab)

  # print(preds)

  preds_and_titleInd = zip(preds, targs)

  sorted_pairs = sorted(preds_and_titleInd)
  sorted_preds = np.sort(preds)[::-1]

  tuples = zip(*sorted_pairs)
  s_preds, s_titleInd = [list(tuple) for tuple in tuples]

  print(s_titleInd[:10])

  top_movies = []
  for i in range(10):
      top_movies.append(new_movies[s_titleInd[i]])

  print(top_movies)
  return jsonify({'text': 'Hello World!'})


@app.route("/movies", methods=['GET'])
def get_movies():
  return data


@app.route("/recommended/<ID>", methods=['GET'])
def recommended(ID):
  path = Path('Hack-Western-7/ml-latest-small')
  model_path = Path('Hack-Western-7/models')

  ratings = pd.read_csv(path / 'ratings.csv')
  movies = pd.read_csv(path / 'movies.csv')

  ratings = ratings.merge(movies)
  ratings = ratings[["userId", "title", "rating"]]

  data_collab = CollabDataLoaders.from_df(ratings, item_name='title', bs=5)

  learn = collab_learner(data_collab, n_factors=50, y_range=(0, 5.5))
  loaded_learner = learn.load('model-1')

  dls = CollabDataLoaders.from_df(ratings, item_name='title', bs=64)

  userId = ID
  rows = []
  rating_ind = 0

  user_watched = ratings[ratings["userId"] == int(userId)]
  print(len(user_watched))
  user_watched_titles = user_watched.loc[:, "title"]
  print(len(user_watched_titles))
  movie_list = np.unique(ratings[['title']])

  new_movies = np.setdiff1d(movie_list, user_watched_titles)
  print(len(new_movies))

  for i in range(len(new_movies)):
    rows.append(dict({'userId': userId, 'title': new_movies[i], 'rating': rating_ind}))
    rating_ind += 1


  test_data = pd.DataFrame(rows)
  print(test_data)

  test_collab = CollabDataLoaders.from_df(test_data, item_name='title', shuffle_train=False, bs=64, valid_pct=0.0,
                                          seed=42)

  preds, targs = loaded_learner.get_preds(dl=test_collab)

  preds_and_titleInd = zip(preds, targs)

  sorted_pairs = sorted(preds_and_titleInd)

  tuples = zip(*sorted_pairs)
  s_preds, s_titleInd = [list(tuple) for tuple in tuples]

  top_movies = {}
  for i in range(10):
    json_movie = {i: new_movies[s_titleInd[i]]}
    top_movies.update(json_movie)

  return top_movies


@app.route("/recommended/<firstID>/<secondID>/<thirdID>/<fourthID>", methods=['GET'])
def recommended(firstID, secondID, thirdID, fourthID):
  #code for multi user recommendations here
  #will need a way to handle empty input, they will come though as an empty string
  return


if __name__ == '__main__':
    app.run(port=5002)

