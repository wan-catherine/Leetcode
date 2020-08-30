from unittest import TestCase
from problems.N1567_Maximum_Length_Of_Subarray_With_Positive_Product import Solution

class TestSolution(TestCase):
    def test_getMaxLen(self):
        self.assertEqual(4, Solution().getMaxLen([1, -2, -3, 4]))

    def test_getMaxLen_1(self):
        nums = [0,1,-2,-3,-4]
        self.assertEqual(3, Solution().getMaxLen(nums))

    def test_getMaxLen_2(self):
        nums = [-1,-2,-3,0,1]
        self.assertEqual(2, Solution().getMaxLen(nums))

    def test_getMaxLen_3(self):
        nums = [-1,2]
        self.assertEqual(1, Solution().getMaxLen(nums))

    def test_getMaxLen_4(self):
        nums = [1,2,3,5,-6,4,0,10]
        self.assertEqual(4, Solution().getMaxLen(nums))

    def test_getMaxLen_5(self):
        nums = [5,-20,-20,-39,-5,0,0,0,36,-32,0,-7,-10,-7,21,20,-12,-34,26,2]
        self.assertEqual(8, Solution().getMaxLen(nums))