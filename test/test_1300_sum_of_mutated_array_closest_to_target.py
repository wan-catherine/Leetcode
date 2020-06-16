from unittest import TestCase
from problems.N1300_Sum_Of_Mutated_Array_Closest_To_Target import Solution

class TestSolution(TestCase):
    def test_findBestValue(self):
        self.assertEqual(3, Solution().findBestValue([4,9,3], 10))

    def test_findBestValue_1(self):
        self.assertEqual(5, Solution().findBestValue([2,3,5], 10))

    def test_findBestValue_2(self):
        self.assertEqual(11361, Solution().findBestValue([60864,25176,27249,21296,20204], 56803))

    def test_findBestValue_3(self):
        self.assertEqual(17422, Solution().findBestValue([1547, 83230, 57084, 93444, 70879], 71237))

    def test_findBestValue_4(self):
        self.assertEqual(15, Solution().findBestValue([15, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 50))
