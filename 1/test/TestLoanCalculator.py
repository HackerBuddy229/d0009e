import unittest
import loanCalculator


class TestLoanCalculator(unittest.TestCase):

    def test_loanCalculator(self):
        cost = loanCalculator.kostnad(50000, 0.03, 10)
        self.assertEqual(cost, 58250)  # add assertion here


if __name__ == '__main__':
    unittest.main()
