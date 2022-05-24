from unittest import TestCase
from problems.N2280_Minimum_Lines_To_Represent_A_Line_Chart import Solution

class TestSolution(TestCase):
    def test_minimum_lines(self):
        self.assertEqual(3, Solution().minimumLines([[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]))

    def test_minimum_lines_1(self):
        self.assertEqual(1, Solution().minimumLines([[3,4],[1,2],[7,8],[2,3]]))

    def test_minimum_lines_2(self):
        self.assertEqual(1, Solution().minimumLines([[1,2],[8,31],[15,60]]))

    def test_minimum_lines_3(self):
        self.assertEqual(1, Solution().minimumLines([[1,3],[2,3],[3,3]]))

    def test_minimum_lines_4(self):
        self.assertEqual(2, Solution().minimumLines([[1,1],[500000000,499999999],[1000000000,999999998]]))
