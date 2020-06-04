from unittest import TestCase
from problems.N769_Max_Chunks_To_Make_Sorted import Solution

class TestSolution(TestCase):
    def test_maxChunksToSorted(self):
        self.assertEqual(1, Solution().maxChunksToSorted([4,3,2,1,0]))

    def test_maxChunksToSorted_1(self):
        self.assertEqual(4, Solution().maxChunksToSorted([1,0,2,3,4]))

    def test_maxChunksToSorted_2(self):
        self.assertEqual(1, Solution().maxChunksToSorted([0]))