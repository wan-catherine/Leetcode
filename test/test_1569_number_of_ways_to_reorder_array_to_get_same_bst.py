from unittest import TestCase
from problems.N1569_Number_Of_Ways_To_Reorder_Array_To_Get_Same_BST import Solution

class TestSolution(TestCase):
    def test_numOfWays(self):
        self.assertEqual(1, Solution().numOfWays([2,1,3]))

    def test_numOfWays_1(self):
        self.assertEqual(5, Solution().numOfWays([3,4,5,1,2]))

    def test_numOfWays_2(self):
        self.assertEqual(0, Solution().numOfWays([1,2,3]))

    def test_numOfWays_3(self):
        self.assertEqual(19, Solution().numOfWays([3,1,2,5,4,6]))

    def test_numOfWays_4(self):
        self.assertEqual(216212978, Solution().numOfWays([9,4,2,1,3,6,5,7,8,14,11,10,12,13,16,15,17,18]))

    def test_numOfWays_5(self):
        self.assertEqual(0, Solution().numOfWays([5,1,4,2,3]))

    def test_numOfWays_6(self):
        self.assertEqual(840839, Solution().numOfWays([6,9,11,15,1,12,3,2,7,8,14,4,5,13,10]))

