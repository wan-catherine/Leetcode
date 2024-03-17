from unittest import TestCase
from problems.N3048_Earliest_Second_To_Mark_Indices_I import Solution

class TestSolution(TestCase):
    def test_earliest_second_to_mark_indices(self):
        self.assertEqual(8, Solution().earliestSecondToMarkIndices(nums = [2,2,0], changeIndices = [2,2,2,2,3,2,2,1]))

    def test_earliest_second_to_mark_indices_1(self):
        self.assertEqual(6, Solution().earliestSecondToMarkIndices(nums = [1,3], changeIndices = [1,1,1,2,1,1,1]))

    def test_earliest_second_to_mark_indices_2(self):
        self.assertEqual(-1, Solution().earliestSecondToMarkIndices(nums = [0,1], changeIndices = [2,2,2]))
