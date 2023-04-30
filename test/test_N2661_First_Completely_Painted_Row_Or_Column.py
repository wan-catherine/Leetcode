from unittest import TestCase
from problems.N2661_First_Completely_Painted_Row_Or_Column import Solution

class TestSolution(TestCase):
    def test_first_complete_index(self):
        self.assertEqual(2, Solution().firstCompleteIndex(arr = [1,3,4,2], mat = [[1,4],[2,3]]))

    def test_first_complete_index_1(self):
        self.assertEqual(3, Solution().firstCompleteIndex(arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]))

    def test_first_complete_index_2(self):
        self.assertEqual(1, Solution().firstCompleteIndex(arr = [1,4,5,2,6,3], mat = [[4,3,5],[1,2,6]]))
