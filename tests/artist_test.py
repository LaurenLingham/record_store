import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):
    def setUp(self):
        self.artist = Artist("Bruce Springsteen", 1)

    def test_artist_has_name(self):
        expected = "Bruce Springsteen"
        actual = self.artist.name
        self.assertEqual(expected, actual)
    
    def test_artist_has_id(self):
        expected = 1
        actual = self.artist.id
        self.assertEqual(expected, actual)
