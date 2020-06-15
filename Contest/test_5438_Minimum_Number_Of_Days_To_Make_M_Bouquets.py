from unittest import TestCase
from .N5438_Minimum_Number_Of_Days_To_Make_M_Bouquets import Solution

class TestSolution(TestCase):
    def test_minDays(self):
        bloomDay = [1, 10, 3, 10, 2]
        m = 3
        k = 1
        res = Solution().minDays(bloomDay, m, k)
        self.assertEqual(3, res)

    def test_minDays_1(self):
        bloomDay = [1, 10, 3, 10, 2]
        m = 3
        k = 2
        res = Solution().minDays(bloomDay, m, k)
        self.assertEqual(-1, res)

    def test_minDays_2(self):
        bloomDay = [7, 7, 7, 7, 12, 7, 7]
        m = 2
        k = 3
        res = Solution().minDays(bloomDay, m, k)
        self.assertEqual(12, res)

    def test_minDays_3(self):
        bloomDay = [1000000000, 1000000000]
        m = 1
        k = 1
        res = Solution().minDays(bloomDay, m, k)
        self.assertEqual(1000000000, res)

    def test_minDays_4(self):
        bloomDay = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
        m = 4
        k = 2
        res = Solution().minDays(bloomDay, m, k)
        self.assertEqual(9, res)
