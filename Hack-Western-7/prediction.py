from fastai.tabular.all import *
from fastai.collab import *
import pickle

path = Path('Hack-Western-7/ml-latest-small')
model_path = Path('Hack-Western-7')

ratings = pd.read_csv(path/'ratings.csv')
movies = pd.read_csv(path/'movies.csv')

ratings = ratings.merge(movies)
ratings = ratings[["userId", "title", "rating"]]

data_collab = CollabDataLoaders.from_df(ratings, item_name='title', bs=5)

learn = collab_learner(data_collab, n_factors=50, y_range=(0, 5.5))
loaded_learner = learn.load('model-1')

dls = CollabDataLoaders.from_df(ratings, item_name='title', bs=64)

userId = 438
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

print(preds)

preds_and_titleInd = zip(preds, targs)

sorted_pairs = sorted(preds_and_titleInd)
sorted_preds = np.sort(preds)[::-1]

tuples = zip(*sorted_pairs)
s_preds, s_titleInd = [list(tuple) for tuple in tuples]

top_movies = []
for i in range(10):
    top_movies.append(new_movies[s_titleInd[i]])

print(top_movies)

pickle.dump(top_movies, open('model.pkl', 'wb'))

model = pickle.load(open('model.pkl', 'rb'))



