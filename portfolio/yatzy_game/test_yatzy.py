# test_yatzy.py
import unittest
from yatzy import Yatzy

class TestYatzy(unittest.TestCase):
    def setUp(self):
        self.y = Yatzy()

    def test_roll(self):
        self.y.roll()
        self.assertEqual(len(self.y.get_dice()), 5)

    def test_scoring_methods(self):
        self.y.dice = [1, 1, 2, 3, 4]
        self.assertEqual(self.y.Ones(), 2)
        self.assertEqual(self.y.Twos(), 2)
        self.assertEqual(self.y.Threes(), 3)
        self.assertEqual(self.y.Fours(), 4)

    def test_one_pair(self):
        self.y.dice = [2, 2, 3, 4, 5]
        self.assertEqual(self.y.OnePair(), 4)

    def test_two_pairs(self):
        self.y.dice = [2, 2, 3, 3, 5]
        self.assertEqual(self.y.TwoPairs(), 10)

    def test_three_alike(self):
        self.y.dice = [4, 4, 4, 2, 1]
        self.assertEqual(self.y.ThreeAlike(), 12)

    def test_four_alike(self):
        self.y.dice = [5, 5, 5, 5, 1]
        self.assertEqual(self.y.FourAlike(), 20)

    def test_small_large(self):
        self.y.dice = [1, 2, 3, 4, 5]
        self.assertEqual(self.y.Small(), 15)
        self.y.dice = [2, 3, 4, 5, 6]
        self.assertEqual(self.y.Large(), 20)

    def test_full_house(self):
        self.y.dice = [3, 3, 3, 2, 2]
        self.assertEqual(self.y.FullHourse(), 13)

    def test_chance(self):
        self.y.dice = [6, 5, 4, 3, 2]
        self.assertEqual(self.y.Chance(), 20)

    def test_yatzy(self):
        self.y.dice = [4, 4, 4, 4, 4]
        self.assertEqual(self.y.Yatzy(), 50)

if __name__ == '__main__':
    unittest.main()
