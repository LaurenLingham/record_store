from flask import render_template, request, redirect
from flask import Blueprint
from models.artist import Artist
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artists_blueprint = Blueprint("artists", __name__)

@artists_blueprint.route("/artists")
def artists():
    artists = artist_repository.select_all()
    return render_template("artists/index.html", artists = artists)

@artists_blueprint.route("/artists/new")
def new_artist():
    return render_template("/artists/new.html")

@artists_blueprint.route("/artists", methods=["POST"])
def create_artist():
    name = request.form["name"]
    artist = Artist(name)
    artist_repository.save(artist)
    return redirect("/artists")

@artists_blueprint.route("/artists/<id>")
def show_artist(id):
    artist = artist_repository.select(id)
    albums = album_repository.filter_by_artist(artist.id)
    return render_template("artists/artist.html", artist = artist, albums = albums)

@artists_blueprint.route("/artists/<id>/edit")
def edit_artist(id):
    artist = artist_repository.select(id)
    return render_template("artists/edit.html", artist = artist)

@artists_blueprint.route("/artists/<id>", methods=["POST"])
def update_artist(id):
    name = request.form["name"]
    artist = Artist(name, id)
    artist_repository.update(artist)
    return redirect("/artists")

@artists_blueprint.route("/artists/<id>/delete", methods=["POST"])
def delete_artist(id):
    artist_repository.delete(id)
    return redirect ("/artists")