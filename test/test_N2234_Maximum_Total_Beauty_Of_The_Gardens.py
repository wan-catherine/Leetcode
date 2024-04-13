from unittest import TestCase
from problems.N2234_Maximum_Total_Beauty_Of_The_Gardens import Solution

class TestSolution(TestCase):
    def test_maximum_beauty(self):
        self.assertEqual(14, Solution().maximumBeauty(flowers = [1,3,1,1], newFlowers = 7, target = 6, full = 12, partial = 1))

    def test_maximum_beauty_1(self):
        self.assertEqual(30, Solution().maximumBeauty(flowers = [2,4,5,3], newFlowers = 10, target = 5, full = 2, partial = 6))

    def test_maximum_beauty_2(self):
        self.assertEqual(14, Solution().maximumBeauty(flowers = [20,1,15,17,10,2,4,16,15,11], newFlowers = 2, target = 20, full = 10, partial = 2))
