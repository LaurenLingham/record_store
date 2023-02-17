from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    artist.id = id
    return artist

def select_all():
    pass

def select(id):
    pass

def update(artist):
    pass
    
def delete_all():
    pass

def delete(id):
    pass

def albums(artist):
    pass