from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from db_handler import *
from form_handler import *
from api_handler import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
Bootstrap(app)


@app.route("/")
def home():
    movie_list = GetData()
    row_count = len(movie_list)
    for movie in movie_list:
        movie[4] = row_count
        row_count -= 1

    return render_template("index.html", movies=movie_list)

@app.route("/edit/<num>", methods=["GET", "POST"])
def edit(num):
    form = UpdateRating()
    if form.validate_on_submit():
        UpdateData(id= int(num),
                    new_rating= form.rating_field.data,
                    new_review= form.review_field.data)
        return redirect(url_for('home'))
    return render_template('edit.html', id=num, form=form)

@app.route("/delete/<id>")
def delete(id):
    RemoveData(id)
    return redirect(url_for('home'))

@app.route("/add", methods=["GET","POST"])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        movie = form.search.data
        return redirect(url_for('select', movie=movie))
    return render_template('add.html', form=form)

@app.route("/select/<movie>")
def select(movie):
    movies_dict = MovieSearch(movie)
    return render_template("select.html", results=movies_dict)

@app.route("/choose/<id>")
def choose(id):
    row_id = IdSearch(id)
    return redirect(url_for('edit', num=row_id))


if __name__ == '__main__':
    app.run()
