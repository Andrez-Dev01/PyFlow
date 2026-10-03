import unittest
from src.reader import load_csv

class TestReader(unittest.TestCase):
    def test_csv_load(self):
        characters = load_csv("data/dragon_ball_z.csv")
        self.assertTrue(len(characters) > 0)

if __name__ == "__main__":
    unittest.main()
