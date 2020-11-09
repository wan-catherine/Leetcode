from unittest import TestCase
from problems.N354_Russian_Doll_Envelopes import Solution

class TestSolution(TestCase):
    def test_maxEnvelopes(self):
        self.assertEqual(3, Solution().maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))

    def test_maxEnvelopes_1(self):
        self.assertEqual(3, Solution().maxEnvelopes([[4,5],[6,7],[2,3]]))
