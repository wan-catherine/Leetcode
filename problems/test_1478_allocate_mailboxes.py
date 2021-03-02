from unittest import TestCase
from problems.N1478_Allocate_Mailboxes import Solution

class TestSolution(TestCase):
    def test_minDistance(self):
        self.assertEqual(5, Solution().minDistance(houses = [1,4,8,10,20], k = 3))

    def test_minDistance_1(self):
        self.assertEqual(8, Solution().minDistance(houses = [7,4,6,1], k = 1))

    def test_minDistance_2(self):
        self.assertEqual(9, Solution().minDistance(houses = [2,3,5,12,18], k = 2))

    def test_minDistance_3(self):
        self.assertEqual(0, Solution().minDistance(houses = [3,6,14,10], k = 4))

    def test_minDistance_4(self):
        self.assertEqual(4, Solution().minDistance([1,8,12,10,3], 3))