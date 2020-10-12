from unittest import TestCase
from problems.N959_Regions_Cut_By_Slashes import Solution

class TestSolution(TestCase):
    def test_regionsBySlashes(self):
        self.assertEqual(2, Solution().regionsBySlashes([" /","/ "]))

    def test_regionsBySlashes_1(self):
        self.assertEqual(1, Solution().regionsBySlashes([" /","  "]))

    def test_regionsBySlashes_2(self):
        self.assertEqual(4, Solution().regionsBySlashes(["\\/","/\\"]))

    def test_regionsBySlashes_3(self):
        self.assertEqual(5, Solution().regionsBySlashes(["/\\","\\/"]))

    def test_regionsBySlashes_4(self):
        self.assertEqual(3, Solution().regionsBySlashes(["//","/ "]))

