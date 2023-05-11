from unittest import TestCase
from problems.N2615_Sum_Of_Distances import Solution

class TestSolution(TestCase):
    def test_distance(self):
        self.assertListEqual([5,0,3,4,0], Solution().distance([1,3,1,1,2]))

    def test_distance_1(self):
        self.assertListEqual([0,0,0], Solution().distance([0,5,3]))
