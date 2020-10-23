from unittest import TestCase
from problems.N849_Maximize_Distance_To_Closest_Person import Solution

class TestSolution(TestCase):
    def test_maxDistToClosest(self):
        self.assertEqual(2, Solution().maxDistToClosest([1,0,0,0,1,0,1]))

    def test_maxDistToClosest_1(self):
        self.assertEqual(3, Solution().maxDistToClosest([1,0,0,0]))

    def test_maxDistToClosest_2(self):
        self.assertEqual(1, Solution().maxDistToClosest([0,1]))
