from unittest import TestCase
from problems.N2401_Longest_Nice_Subarray import Solution

class TestSolution(TestCase):
    def test_longest_nice_subarray(self):
        self.assertEquals(3, Solution().longestNiceSubarray([1,3,8,48,10]))

    def test_longest_nice_subarray_1(self):
        self.assertEquals(1, Solution().longestNiceSubarray([3,1,5,11,13]))
