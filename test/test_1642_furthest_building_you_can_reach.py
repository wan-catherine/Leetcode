from unittest import TestCase
from problems.N1642_Furthest_Building_You_Can_Reach import Solution

class TestSolution(TestCase):
    def test_furthestBuilding(self):
        self.assertEqual(4, Solution().furthestBuilding(heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1))

    def test_furthestBuilding_1(self):
        self.assertEqual(7, Solution().furthestBuilding(heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2))

    def test_furthestBuilding_2(self):
        self.assertEqual(3, Solution().furthestBuilding(heights = [14,3,19,3], bricks = 17, ladders = 0))

    def test_furthestBuilding_3(self):
        self.assertEqual(1, Solution().furthestBuilding(heights = [7,5,13], bricks = 0, ladders = 0))

    def test_furthestBuilding_4(self):
        self.assertEqual(0, Solution().furthestBuilding(heights = [1,2], bricks = 0, ladders = 0))