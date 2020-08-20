from unittest import TestCase
from problems.N583_Delete_Operation_For_Two_Strings import Solution

class TestSolution(TestCase):
    def test_minDistance(self):
        self.assertEqual(2, Solution().minDistance("sea", "eat"))

    def test_minDistance_1(self):
        self.assertEqual(1, Solution().minDistance("a", "ab"))
