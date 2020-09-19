from unittest import TestCase
from problems.N935_Knight_Dialer import Solution

class TestSolution(TestCase):
    def test_knightDialer(self):
        self.assertEqual(10, Solution().knightDialer(1))

    def test_knightDialer_1(self):
        self.assertEqual(20, Solution().knightDialer(2))

    def test_knightDialer_2(self):
        self.assertEqual(46, Solution().knightDialer(3))

    def test_knightDialer_3(self):
        self.assertEqual(136006598, Solution().knightDialer(3131))

