from unittest import TestCase
from problems.N1883_Minimum_Skips_To_Arrive_At_Meeting_On_Time import Solution

class TestSolution(TestCase):
    def test_min_skips(self):
        self.assertEqual(1, Solution().minSkips(dist = [1,3,2], speed = 4, hoursBefore = 2))

    def test_min_skips_1(self):
        self.assertEqual(2, Solution().minSkips(dist = [7,3,5,5], speed = 2, hoursBefore = 10))

    def test_min_skips_2(self):
        self.assertEqual(-1, Solution().minSkips(dist = [7,3,5,5], speed = 1, hoursBefore = 10))

    def test_min_skips_3(self):
        self.assertEqual(4, Solution().minSkips([1,1,1,1,1], 1000000, 1))

    def test_min_skips_4(self):
        self.assertEqual(0, Solution().minSkips([7,6,5,3,4,6,2,2,7,2], 5, 17))
