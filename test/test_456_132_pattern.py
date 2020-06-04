from unittest import TestCase
from problems.N456_132_Pattern import Solution

class TestSolution(TestCase):
    def test_find132pattern(self):
        self.assertFalse(Solution().find132pattern([1, 2, 3, 4]))

    def test_find132pattern_1(self):
        self.assertTrue(Solution().find132pattern([3, 1, 4, 2]))

    def test_find132pattern_2(self):
        self.assertTrue(Solution().find132pattern([-1, 3, 2, 0]))

    def test_find132pattern_3(self):
        self.assertTrue(Solution().find132pattern([3,5,0,3,4]))
