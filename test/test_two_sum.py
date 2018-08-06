from unittest import TestCase
from problems.TwoSum import Solution

class TestTwoSum(TestCase):
    def test_two_sum_with_result(self):
        nums = [2, 7, 11, 15]
        solution = Solution()
        self.assertListEqual([0,1], solution.twoSum(nums, 9))

    def test_two_sum_with_two_zero(self):
        nums = [0,0]
        solution = Solution()
        self.assertListEqual([0,1], solution.twoSum(nums, 0))

    def test_two_sum_with_negetive_integers(self):
        nums = [-5,7, 9,0,2,-4]
        solution = Solution()
        self.assertListEqual([1,5], solution.twoSum(nums, 3))

    def test_two_sum_with_another_negetive_integers(self):
        nums = [7, -5, 9,-4,2,0]
        solution = Solution()
        self.assertListEqual([0,3], solution.twoSum(nums, 3))

    def test_two_sum_with_same__integers(self):
        nums = [7, -5, 9,-4,2,9, -3]
        solution = Solution()
        self.assertListEqual([2,5], solution.twoSum(nums, 18))