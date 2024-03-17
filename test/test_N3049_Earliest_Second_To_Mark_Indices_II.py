from unittest import TestCase
from problems.N3049_Earliest_Second_To_Mark_Indices_II import Solution

class TestSolution(TestCase):
    def test_earliest_second_to_mark_indices(self):
        self.assertEqual(6, Solution().earliestSecondToMarkIndices(nums = [3,2,3], changeIndices = [1,3,2,2,2,2,3]))

    def test_earliest_second_to_mark_indices_1(self):
        self.assertEqual(7, Solution().earliestSecondToMarkIndices(nums = [0,0,1,2], changeIndices = [1,2,1,2,1,2,1,2]))

    def test_earliest_second_to_mark_indices_2(self):
        self.assertEqual(-1, Solution().earliestSecondToMarkIndices(nums = [1,2,3], changeIndices = [1,2,3]))
