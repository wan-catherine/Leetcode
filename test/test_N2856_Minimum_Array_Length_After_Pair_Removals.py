from unittest import TestCase
from problems.N2856_Minimum_Array_Length_After_Pair_Removals import Solution

class TestSolution(TestCase):
    def test_min_length_after_removals(self):
        self.assertEquals(0, Solution().minLengthAfterRemovals([1,3,4,9]))

    def test_min_length_after_removals_1(self):
        self.assertEquals(0, Solution().minLengthAfterRemovals([2,3,6,9]))

    def test_min_length_after_removals_2(self):
        self.assertEquals(1, Solution().minLengthAfterRemovals([1,1,2]))

    def test_min_length_after_removals_3(self):
        self.assertEquals(0, Solution().minLengthAfterRemovals([1,1,2,3,4,4]))

    def test_min_length_after_removals_4(self):
        self.assertEquals(0, Solution().minLengthAfterRemovals([1,1,4,4,5,5]))
