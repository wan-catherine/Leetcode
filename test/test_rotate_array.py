from unittest import TestCase
from problems.RotateArray import Solution

class TestSolution(TestCase):
    def test_rotate(self):
        solution = Solution()
        nums = [1,2,3,4,5,6,7]
        solution.rotate(nums, 3)
        self.assertEqual(nums,[5,6,7,1,2,3,4] )
