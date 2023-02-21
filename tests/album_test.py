import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):
    def setUp(self):
        self.album = Album("Bruce Springsteen", "Born in the U.S.A.", 1984, "Rock",
                           10, 5.00, 10.00)

    def test_album_has_artist(self):
        expected = "Bruce Springsteen"
        actual = self.album.artist
        self.assertEqual(expected, actual)
    
    def test_album_has_title(self):
        expected = "Born in the U.S.A."
        actual = self.album.title
        self.assertEqual(expected, actual)
    
    def test_album_has_year_released(self):
        expected = 1984
        actual = self.album.year_released
        self.assertEqual(expected, actual)

    def test_album_has_genre(self):
        expected = "Rock"
        actual = self.album.genre
        self.assertEqual(expected, actual)
    
    def test_album_has_stock(self):
        expected = 10
        actual = self.album.stock_qty
        self.assertEqual(expected, actual)

    def test_album_has_stock(self):
        expected = 5.00
        actual = self.album.purchase_price
        self.assertEqual(expected, actual)

    def test_album_has_name(self):
        expected = 10.00
        actual = self.album.sell_price
        self.assertEqual(expected, actual)
    