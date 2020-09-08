from unittest import TestCase
from problems.N658_Find_K_Closest_Elements import Solution

class TestSolution(TestCase):
    def test_findClosestElements(self):
        self.assertListEqual([1,2,3,4], Solution().findClosestElements([1,2,3,4,5], k = 4, x = 3))

    def test_findClosestElements_1(self):
        self.assertListEqual([1,2,3,4], Solution().findClosestElements([1,2,3,4,5], k = 4, x = -1))

    def test_findClosestElements_2(self):
        self.assertListEqual([3,3,4], Solution().findClosestElements([0,0,1,2,3,3,4,7,7,8], 3, 5))
