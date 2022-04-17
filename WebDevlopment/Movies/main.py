from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FloatField
from wtforms.validators import DataRequired, Email, Length
import requests

MOVIE_ENDPOINT = "https://api.themoviedb.org/3/search/movie"
TMDB_ENDPOINT = 'https://api.themoviedb.org/3'
API_KEY = "00a03104170d378e428ff62054eea698"
MOVIE_DB_IMG_URL = 'https://image.tmdb.org/t/p/w500/'
TMDB_BEARER_TOKEN = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwMGEwMzEwNDE3MGQzNzhlNDI4ZmY2MjA1NGVlYTY5OCIsInN1YiI6IjYyNTlhNTUzZWNhZWY1MTVmZjY3N2RlYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.e55CkUSERLZy_DXAyhzCEKqXXTFJ-7VnTC_wAhXrdCU'

class UpdateForm(FlaskForm):
    rating = FloatField(label='Rating out of 10 e.g. 7.8')
    review = StringField(label='Your Review')
    submit = SubmitField(label="Done")


class AddMovie(FlaskForm):
    title = StringField(label='Movie Title: ')
    submit = SubmitField(label="Add Movie")


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

##CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

db.create_all()

# After adding the new_movie the code needs to be commented out/deleted.
# So you are not trying to add the same movie twice.
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )


# db.session.add(new_movie)
# db.session.commit()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(0, len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)
    # ---------------------------------------------------------
    # all_movies = Movie.query.order_by(Movie.rating).all()
    # movie_total = Movie.query.count()
    # for movie in all_movies:
    #     movie.ranking = movie_total
    #     db.session.commit()
    #     movie_total -= 1
    # return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    update_form = UpdateForm()
    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)
    if update_form.validate_on_submit():
        movie.rating = update_form.rating.data
        movie.review = update_form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=update_form, movie = movie)


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    movie_id = request.args.get('id')

    # DELETE A RECORD BY ID
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    add_movie = AddMovie()
    if add_movie.validate_on_submit():
        movie_title = add_movie.title.data
        print(movie_title)
        params = {
            'api_key' : API_KEY,
            'query': movie_title
        }

        header = {
            'Authorization': f'Bearer {TMDB_BEARER_TOKEN}',
            'Content-Type': 'application/json;charset=utf-8',
        }

        Movie_res = requests.get(MOVIE_ENDPOINT, params=params, headers=header)
        data = Movie_res.json()["results"]
        print(data)
        return render_template('select.html', options=data)

    return render_template('add.html', form=add_movie)

@app.route('/find', methods=['GET', 'POST'])
def find_movie():
    movie_api_id = request.args.get('id')
    if movie_api_id:

        movie_url = f"{TMDB_ENDPOINT}/movie/{movie_api_id}"

        params = {
            'api_key': API_KEY,
            'language': 'en-US'
        }
        res = requests.get(movie_url, params=params)
        data = res.json()
        newMovie = Movie(
            title = data["title"],
            year = data['release_date'].split('-')[0],
            img_url=f"{MOVIE_DB_IMG_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(newMovie)
        db.session.commit()
        return redirect(url_for('edit', id=newMovie.id))

if __name__ == '__main__':
    app.run(debug=True)
