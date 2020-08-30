from unittest import TestCase
from problems.N473_Matchsticks_To_Square import Solution

class TestSolution(TestCase):
    def test_makesquare(self):
        self.assertTrue(Solution().makesquare([1,1,2,2,2]))

    def test_makesquare_1(self):
        self.assertFalse(Solution().makesquare([3,3,3,3,4]))

    def test_makesquare_2(self):
        self.assertTrue(Solution().makesquare([5,5,5,5,4,4,4,4,3,3,3,3]))
