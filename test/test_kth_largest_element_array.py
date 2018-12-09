from unittest import TestCase
from problems.KthLargestElementArray import Solution

class TestSolution(TestCase):
    def test_findKthLargest(self):
        solution = Solution()
        res = solution.findKthLargest([3,2,1,5,6,4], 2)
        self.assertEqual(5, res)

    def test_findKthLargest_one(self):
        solution = Solution()
        res = solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4)
        self.assertEqual(4, res)
