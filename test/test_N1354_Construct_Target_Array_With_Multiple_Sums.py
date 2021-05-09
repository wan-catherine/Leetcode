from unittest import TestCase
from problems.N1354_Construct_Target_Array_With_Multiple_Sums import Solution

class TestSolution(TestCase):
    def test_is_possible(self):
        self.assertTrue(Solution().isPossible([9,3,5]))

    def test_is_possible_1(self):
        self.assertFalse(Solution().isPossible([1,1,1,2]))

    def test_is_possible_2(self):
        self.assertTrue(Solution().isPossible([8,5]))

    def test_is_possible_3(self):
        self.assertTrue(Solution().isPossible([1,1000000000]))

    def test_is_possible_4(self):
        self.assertTrue(Solution().isPossible([1,1,85,13,43,1,1]))

