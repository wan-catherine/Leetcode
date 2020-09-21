from unittest import TestCase
from problems.N1595_Minimum_Cost_To_Connect_Two_Groups_Of_Points import Solution

class TestSolution(TestCase):
    def test_connectTwoGroups(self):
        self.assertEqual(17, Solution().connectTwoGroups([[15, 96], [36, 2]]))

    def test_connectTwoGroups_1(self):
        self.assertEqual(4, Solution().connectTwoGroups([[1, 3, 5], [4, 1, 1], [1, 5, 3]]))

    def test_connectTwoGroups_2(self):
        self.assertEqual(10, Solution().connectTwoGroups([[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]))

    def test_connectTwoGroups_3(self):
        self.assertEqual(140, Solution().connectTwoGroups([[80,84,73,66,59],[31,82,36,11,47],[10,81,49,45,14],[88,35,28,6,44],[6,23,61,22,69],[41,68,11,33,65],[6,22,48,75,38],[91,80,27,15,93]]))