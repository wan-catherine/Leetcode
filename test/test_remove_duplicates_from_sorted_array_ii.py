from unittest import TestCase
from problems.RemoveDuplicatesfromSortedArrayII import Solution

class TestSolution(TestCase):
    def test_removeDuplicates(self):
        solution = Solution()
        res = solution.removeDuplicates([1,1,1,2,2,3])
        self.assertEqual(5, res)

    def test_removeDuplicates_more(self):
        solution = Solution()
        res = solution.removeDuplicates([0,0,1,1,1,1,2,3,3])
        self.assertEqual(7, res)

    def test_removeDuplicates_check(self):
        solution = Solution()
        nums = [0,0,1,1,1,1,2,3,3]
        res = solution.removeDuplicates(nums)
        self.assertEqual(7, res)
        self.assertEqual(nums[0:7], [0,0,1,1,2,3,3])

    def test_removeDuplicates_dup(self):
        solution = Solution()
        nums = [1,1,1]
        res = solution.removeDuplicates(nums)
        self.assertEqual(2, res)

    def test_removeDuplicates_3(self):
        solution = Solution()
        nums = [1,1,1,1,2,2,3]
        res = solution.removeDuplicates(nums)
        self.assertEqual(5, res)
        self.assertEqual(nums[0:5], [1,1,2,2,3])