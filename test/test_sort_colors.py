from unittest import TestCase
from problems.SortColors import Solution

class TestSolution(TestCase):
    def test_sortColors(self):
        solution = Solution()
        input = [2,0,2,1,1,0]
        solution.sortColors(input)
        self.assertEqual([0,0,1,1,2,2], input)

    def test_sortColors_1(self):
        solution = Solution()
        input = [2,0,1]
        solution.sortColors(input)
        self.assertEqual([0,1,2], input)

    def test_sortColors_0(self):
        solution = Solution()
        input = [0]
        solution.sortColors(input)
        self.assertEqual([0], input)
