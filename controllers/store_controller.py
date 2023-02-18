from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.album import Album
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

albums_blueprint = Blueprint("albums", __name__)

@albums_blueprint.route("/")
def homepage():
    albums = album_repository.select_all()
    total_albums_in_stock = album_repository.total_albums_in_stock(albums)
    total_spend_on_stock = album_repository.total_spend_on_stock(albums)
    return render_template("/index.html", albums = albums, total_albums_in_stock = total_albums_in_stock, total_spend_on_stock = total_spend_on_stock)

@albums_blueprint.route("/albums")
def albums():
    albums = album_repository.select_all()
    return render_template("albums/index.html", all_albums = albums)

@albums_blueprint.route("/albums/new")
def new_album():
    artists = artist_repository.select_all()
    return render_template("/albums/new.html", all_artists = artists)

@albums_blueprint.route("/albums", methods=["POST"])
def create_album():
    artist = artist_repository.select(request.form["artist_id"])
    title = request.form["title"]
    year_released = request.form["year_released"]
    genre = request.form["genre"]
    stock_qty = request.form["stock_qty"]
    purchase_price = request.form["purchase_price"]
    sell_price = request.form["sell_price"]
    album = Album(artist, title, year_released, genre, stock_qty, purchase_price, sell_price)
    album_repository.save(album)
    return redirect("/albums")

@albums_blueprint.route("/albums/<id>")
def show_album(id):
    album = album_repository.select(id)
    return render_template("albums/album.html", album = album)

@albums_blueprint.route("/albums/<id>/edit")
def edit_album(id):
    album = album_repository.select(id)
    artists = artist_repository.select_all()
    return render_template("albums/edit.html", album = album, all_artists = artists)

@albums_blueprint.route("/albums/<id>", methods=["POST"])
def update_album(id):
    artist = artist_repository.select(request.form["artist_id"])
    title = request.form["title"]
    year_released = request.form["year_released"]
    genre = request.form["genre"]
    stock_qty = request.form["stock_qty"]
    purchase_price = request.form["purchase_price"]
    sell_price = request.form["sell_price"]
    album = Album(artist, title, year_released, genre, stock_qty, purchase_price, sell_price)
    print(album.artist.name())
    album_repository.updte(album)
    return redirect("/albums")

@albums_blueprint.route("/albums/<id>/delete", methods=["POST"])
def delete_album(id):
    album_repository.delete(id)
    return redirect ("/albums")
