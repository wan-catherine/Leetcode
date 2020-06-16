from unittest import TestCase
from problems.N1011_Capacity_To_Ship_Packages_Within_D_Days import Solution

class TestSolution(TestCase):
    def test_shipWithinDays(self):
        self.assertEqual(15, Solution().shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))

    def test_shipWithinDays_1(self):
        self.assertEqual(6, Solution().shipWithinDays([3,2,2,4,1,4], 3))

    def test_shipWithinDays_2(self):
        self.assertEqual(3, Solution().shipWithinDays([1,2,3,1,1], 4))
