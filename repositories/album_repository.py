from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repository

Album(["artist_id"], ["title"], ["year_released"], ["genre"], ["stock_qty"], ["purchase_price"], ["sell_price"], ["id"])