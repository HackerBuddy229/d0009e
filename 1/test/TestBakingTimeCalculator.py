import unittest
import BakingTimeCalculator


class TestBakingTimeCalculator(unittest.TestCase):
    def test_mixing_time_calculator(self):
        time = BakingTimeCalculator.tid_blanda(5)
        self.assertEqual(time, 15)  # add assertion here

    def test_baking_time_calculator(self):
        time = BakingTimeCalculator.tid_grädda(5)
        self.assertEqual(time, 45)  # add assertion here


if __name__ == '__main__':
    unittest.main()
