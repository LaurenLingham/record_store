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
    pass

def select(id):
    pass

def update(album):
    pass

def delete_all():
    pass

def delete(id):
    pass


Album(["artist_id"], ["title"], ["year_released"], ["genre"], ["stock_qty"], ["purchase_price"], ["sell_price"], ["id"])