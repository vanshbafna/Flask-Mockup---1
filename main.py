from flask import Flask, jsonify, request
from csv import reader

all_articles = []


# read csv file as a list of lists
with open('articles.csv',  encoding="utf8") as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    data = list(csv_reader)
    print(data[1])
    all_articles = data[1:]


liked_articles = []
not_liked_articles = []
did_not_watch = []

app = Flask(__name__)


@app.route("/get-articles")
def get_articles():
   return jsonify({
       "data": all_articles[0],
       "status": "success"
   })

@app.route("/liked-articles", methods=["POST"])
def liked_articles():
    articles = all_articles[0]
    all_mvies = all_articles[1:]
    liked_articles.append(movie)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-movie", methods=["POST"])
def unliked_movie():
    movie = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(movie)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/did-not-watch", methods=["POST"])
def did_not_watch():
    movie = all_articles[0]
    all_articles = all_articles[1:]
    did_not_watch.append(movie)
    return jsonify({
        "status": "success"
    }), 201

if __name__ == "__main__":
  app.run()