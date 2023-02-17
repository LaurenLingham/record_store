from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.album import Album
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

store_blueprint = Blueprint("record store", __name__)

@store_blueprint.route("/index.html")
def homepage():
    show_inventory = album_repository.select_all()
    total_albums_in_stock = album_repository.total_albums_in_stock(show_inventory)
    total_spend_on_stock = album_repository.total_spend_on_stock(show_inventory)
    return render_template("/index.html", show_inventory = show_inventory, total_albums_in_stock = total_albums_in_stock, total_spend_on_stock = total_spend_on_stock)

@store_blueprint.route("/albums")
def albums():
    albums = album_repository.select_all()
    return render_template("albums/index.html", all_albums = albums)

@store_blueprint.route("albums/new")
def new_album():
    artists = artist_repository.select_all()
    return render_template("albums/new.html", all_artists = artists)

@store_blueprint.route("/albums", methods=["POST"])
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

