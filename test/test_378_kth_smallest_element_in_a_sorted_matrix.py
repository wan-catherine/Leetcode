from unittest import TestCase
from problems.N378_Kth_Smallest_Element_In_A_Sorted_Matrix import Solution

class TestSolution(TestCase):
    def test_kthSmallest(self):
        matrix = [
                     [1, 5, 9],
                     [10, 11, 13],
                     [12, 13, 15]
                 ]
        k = 8
        self.assertEqual(13, Solution().kthSmallest(matrix, k))

    def test_kthSmallest_1(self):
        matrix = [[-5]]
        k = 1
        self.assertEqual(-5, Solution().kthSmallest(matrix, k))

    def test_kthSmallest_2(self):
        matrix = [[1,2],[1,3]]
        k = 2
        self.assertEqual(1, Solution().kthSmallest(matrix, k))

    def test_kthSmallest_3(self):
        matrix =[[1,3,5],[6,7,12],[11,14,14]]
        k = 3
        self.assertEqual(5, Solution().kthSmallest(matrix, k))

    def test_kthSmallest_4(self):
        matrix =[[5,6,9,14,17,17,19],[8,10,14,15,21,24,28],[8,10,16,21,21,26,33],[13,17,17,23,26,27,33],[16,22,23,27,31,31,34],[16,26,28,30,32,32,37],[19,31,35,35,39,44,44]]
        k = 38
        self.assertEqual(31, Solution().kthSmallest(matrix, k))
