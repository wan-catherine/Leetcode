from unittest import TestCase
from problems.N1442_Count_Triplet_That_Can_Form_Two_Arrays_Of_Equal_XOR import Solution

class TestSolution(TestCase):
    def test_countTriplets(self):
        self.assertEqual(4, Solution().countTriplets([2,3,1,6,7]))

    def test_countTriplets_1(self):
        self.assertEqual(10, Solution().countTriplets([1,1,1,1,1]))

    def test_countTriplets_2(self):
        self.assertEqual(0, Solution().countTriplets([2,3]))

    def test_countTriplets_3(self):
        self.assertEqual(3, Solution().countTriplets([1,3,5,7,9]))

    def test_countTriplets_4(self):
        self.assertEqual(8, Solution().countTriplets([7,11,12,9,5,2,7,17,22]))
