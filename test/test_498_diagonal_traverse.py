from unittest import TestCase
from problems.N498_Diagonal_Traverse import Solution

class TestSolution(TestCase):
    def test_findDiagonalOrder(self):
        self.assertListEqual([1,2,4,7,5,3,6,8,9], Solution().findDiagonalOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))
