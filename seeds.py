from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Biffy Clyro")
artist_repository.save(artist_1)

artist_2 = Artist("Brand New")
artist_repository.save(artist_2)


album_1 = Album(artist_1, "Opposites", 2018, "Rock", 10, 6.50, 11.99)
album_repository.save(album_1)

album_2 = Album(artist_1, "Blackened Sky", 2002, "Rock", 4, 5.00, 8.99)
album_repository.save(album_2)

album_3 = Album(artist_2, "The Devil and God Are Raging Inside Me", 2006, "Alt rock", 5, 6.00, 9.99)
album_repository.save(album_3)