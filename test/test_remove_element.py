from unittest import TestCase
from problems.RemoveElement import Solution

class TestSolution(TestCase):
    def test_removeElement(self):
        solution = Solution()
        res = solution.removeElement([3,2,2,3], 2)
        self.assertEqual(res, 2)
