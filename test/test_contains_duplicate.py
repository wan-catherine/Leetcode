from unittest import TestCase
from problems.ContainsDuplicate import Solution

class TestSolution(TestCase):
    def test_containsDuplicate(self):
        solution = Solution()
        res = solution.containsDuplicate([1,2,3,1])
        self.assertEqual(True, res)
