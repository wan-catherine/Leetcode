from unittest import TestCase
from problems.N1552_Magnetic_Force_Between_Two_Balls import Solution

class TestSolution(TestCase):
    def test_maxDistance(self):
        self.assertEqual(3, Solution().maxDistance(position = [1,2,3,4,7], m = 3))

    def test_maxDistance_1(self):
        self.assertEqual(999999999, Solution().maxDistance(position = [5,4,3,2,1,1000000000], m = 2))

    def test_maxDistance_2(self):
        self.assertEqual(5, Solution().maxDistance(position = [79,74,57,22], m = 4))

    def test_maxDistance_3(self):
        self.assertEqual(3, Solution().maxDistance(position = [1,2,3,4,5,6,7,8,9,10], m = 4))
