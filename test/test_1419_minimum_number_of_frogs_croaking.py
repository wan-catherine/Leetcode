from unittest import TestCase
from problems.N1419_Minimum_Number_Of_Frogs_Croaking import Solution

class TestSolution(TestCase):
    def test_minNumberOfFrogs(self):
        self.assertEqual(1, Solution().minNumberOfFrogs("croakcroak"))

    def test_minNumberOfFrogs_1(self):
        self.assertEqual(2, Solution().minNumberOfFrogs("crcoakroak"))

    def test_minNumberOfFrogs_2(self):
        self.assertEqual(-1, Solution().minNumberOfFrogs("croakcrook"))

    def test_minNumberOfFrogs_3(self):
        self.assertEqual(-1, Solution().minNumberOfFrogs("croakcroa"))
