from unittest import TestCase
from problems.N2279_Maximum_Bags_With_Full_Capacity_Of_Rocks import Solution

class TestSolution(TestCase):
    def test_maximum_bags(self):
        self.assertEqual(3, Solution().maximumBags(capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2))

    def test_maximum_bags_1(self):
        self.assertEqual(3, Solution().maximumBags(capacity = [10,2,2], rocks = [2,2,0], additionalRocks = 100))
