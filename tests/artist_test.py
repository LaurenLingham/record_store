import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):
    def setUp(self):
        self.artist = Artist("Bruce Springsteen")

    def test_artist_has_name(self):
        expected = "Bruce Springsteen"
        actual = self.artist.name
        self.assertEqual(expected, actual)
