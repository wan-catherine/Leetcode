from unittest import TestCase
from problems.N1889_Minimum_Space_Wasted_From_Packaging import Solution

class TestSolution(TestCase):
    def test_min_wasted_space(self):
        self.assertEqual(6, Solution().minWastedSpace(packages = [2,3,5], boxes = [[4,8],[2,8]]))

    def test_min_wasted_space_1(self):
        self.assertEqual(-1, Solution().minWastedSpace(packages = [2,3,5], boxes = [[1,4],[2,3],[3,4]]))

    def test_min_wasted_space_2(self):
        self.assertEqual(9, Solution().minWastedSpace(packages = [3,5,8,10,11,12], boxes = [[12],[11,9],[10,5,14]]))

    def test_min_wasted_space_3(self):
        self.assertEqual(4322, Solution().minWastedSpace([341,170,320,161,340,64,369,154,260,159,342,210,168,207,357,152,284,66,99,216,341,195,347,384,90,316,292,155,208,281,1,156,147,108,221,297,311,336,165,239,227,227,346,110,262,243,377,87,338,44,146,264,340,325,318,172,48,385,121,345,159,116,102,76,13,24,126,244,313,394,38,234,213,323,295,100,368,357,197,254,205,125,76,336,353,3,385,395,55,399,218,113,91,357,266,238,26,286,128,63]
, [[69,238,342,272,287,305,163,387],[314,369,259,219,281,229,82,381],[231,133,385,127,327,142,393,399],[249,321,123,141,226,40,366,147,121],[172,164,277,42,71],[119,197,356],[362,110,33],[209,170,278,239,213,32,106],[200,395,300,357,11,392,295],[245,4,181,153,386,200,215]]))
