from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.album import Album
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

albums_blueprint = Blueprint("albums", __name__)

@albums_blueprint.route("/albums")
def albums():
    albums = album_repository.select_all()
    return render_template("albums/index.html")

@albums_blueprint.route("albums/new")
def new_album():
    artists = artist_repository.select_all()
    return render_template("albums/new.html", all_artists = artists)

@albums_blueprint.route("/books", methods=["POST"])
def create_book():
    pass