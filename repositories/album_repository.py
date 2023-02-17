from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repository


def save(album):
    sql = """INSERT INTO books (artist_id, title, year_released, genre, stock_qty, purchase_price, sell_price)
            VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"""
    values = [album.artist.id, album.title, album.year_released, album.genre, album.stock_qty, album.purchase_price, album.sell_price]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        artist = artist_repository.select(row["artist_id"])
        album = Album(artist, row["title"], row["year_released"], row["genre"], row["stock_qty"], row["purchase_price"], row["sell_price"], row["id"])
        albums.append(album)
    return albums

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        artist = artist_repository.select(result["artist_id"])
        album = Album(artist, result["title"], result["year_released"], result["genre"], result["stock_qty"], result["purchase_price"], result["sell_price"], result["id"])
    return album

def update(album):
    sql = """UPDATE albums SET (artist_id, title, year_released, genre, stock_qty, purchase_price, sell_price)
            = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"""
    values = [album.artist.id, album.title, album.year_released, album.genre, album.stock_qty, album.purchase_price, album.sell_price, album.id]
    print(values)
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def filter_by_artist(id):
    albums = []
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        artist = artist_repository.select(row["artist_id"])
        album = Album(artist, row["title"], row["year_released"], row["genre"], row["stock_qty"], row["purchase_price"], row["sell_price"], row["id"])
        albums.append(album)
    return albums

def markup(purchase_price, sell_price):
    diff = abs(purchase_price - sell_price)
    avg = (purchase_price + sell_price) / 2
    return round((diff / avg) * 100)

def total_albums_in_stock(albums):
    total_albums = 0
    for album in albums:
        total_albums += album.stock_qty
    return total_albums
