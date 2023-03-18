import unittest

from domain.entities import TvShow


class TestCaseTvShow(unittest.TestCase):
    def test_create_show(self):
        show = TvShow('COM21', 'The Good Place', 'fantasy comedy', 53)
        self.assertTrue(show.get_show_id() == 'COM21')
        self.assertEqual(show.get_title(), 'The Good Place')
        self.assertEqual(show.get_genre(), 'fantasy comedy')
        self.assertTrue(show.get_no_eps() == 53)

    def test_update_atr(self):
        show = TvShow('COM21', 'The Good Place', 'fantasy comedy', 53)
        show.set_show_id('DER65')
        show.set_no_eps(43)
        show.set_genre('fantasy romance')
        self.assertTrue(show.get_show_id() == 'DER65')
        self.assertEqual(show.get_title(), 'The Good Place')
        self.assertEqual(show.get_genre(), 'fantasy romance')
        self.assertTrue(show.get_no_eps() == 43)