from unittest import TestCase
from problems.N969_Pancake_Sorting import Solution

class TestSolution(TestCase):
    def test_pancakeSort(self):
        self.assertListEqual([3, 4, 2, 3, 2], Solution().pancakeSort([3,2,4,1]))

    def test_pancakeSort_1(self):
        self.assertListEqual([], Solution().pancakeSort([1,2,3]))
