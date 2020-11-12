from unittest import TestCase
from problems.N363_Max_Sum_Of_Rectangle_No_Larger_Than_K import Solution

class TestSolution(TestCase):
    def test_maxSumSubmatrix(self):
        self.assertEqual(2, Solution().maxSumSubmatrix(matrix = [[1,0,1],[0,-2,3]], k = 2))

    def test_maxSumSubmatrix_1(self):
        self.assertEqual(3, Solution().maxSumSubmatrix([[2,2,-1]], 3))

    def test_maxSumSubmatrix_2(self):
        self.assertEqual(-1, Solution().maxSumSubmatrix([[2,2,-1]], 0))

    def test_maxSumSubmatrix_3(self):
        self.assertEqual(2, Solution().maxSumSubmatrix([[2,2,-1]], 2))

    def test_maxSumSubmatrix_4(self):
        self.assertEqual(2, Solution().maxSumSubmatrix([[2,4,-2]], 3))

    def test_maxSumSubmatrix_5(self):
        self.assertEqual(12, Solution().maxSumSubmatrix([[7,7,4,-6,-10],[-7,-3,-9,-1,-7],[9,6,-3,-7,7],[-4,1,4,-3,-8],[-7,-4,-4,6,-10],[1,3,-2,3,-10],[8,-2,1,1,-8]], 12))

    def test_maxSumSubmatrix_6(self):
        self.assertEqual(-101, Solution().maxSumSubmatrix([[27,5,-20,-9,1,26,1,12,7,-4,8,7,-1,5,8],[16,28,8,3,16,28,-10,-7,-5,-13,7,9,20,-9,26],[24,-14,20,23,25,-16,-15,8,8,-6,-14,-6,12,-19,-13],[28,13,-17,20,-3,-18,12,5,1,25,25,-14,22,17,12],[7,29,-12,5,-5,26,-5,10,-5,24,-9,-19,20,0,18],[-7,-11,-8,12,19,18,-15,17,7,-1,-11,-10,-1,25,17],[-3,-20,-20,-7,14,-12,22,1,-9,11,14,-16,-5,-12,14],[-20,-4,-17,3,3,-18,22,-13,-1,16,-11,29,17,-2,22],[23,-15,24,26,28,-13,10,18,-6,29,27,-19,-19,-8,0],[5,9,23,11,-4,-20,18,29,-6,-4,-11,21,-6,24,12],[13,16,0,-20,22,21,26,-3,15,14,26,17,19,20,-5],[15,1,22,-6,1,-9,0,21,12,27,5,8,8,18,-1],[15,29,13,6,-11,7,-6,27,22,18,22,-3,-9,20,14],[26,-6,12,-10,0,26,10,1,11,-10,-16,-18,29,8,-8],[-19,14,15,18,-10,24,-9,-7,-19,-14,23,23,17,-5,6]]
,-100))