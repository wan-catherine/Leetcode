from unittest import TestCase
from problems.N1591_Strange_Printer_II import Solution

class TestSolution(TestCase):
    def test_isPrintable(self):
        self.assertTrue(Solution().isPrintable([[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]))

    def test_isPrintable_1(self):
        self.assertTrue(Solution().isPrintable([[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]))

    def test_isPrintable_2(self):
        self.assertFalse(Solution().isPrintable([[1,2,1],[2,1,2],[1,2,1]]))

    def test_isPrintable_3(self):
        self.assertFalse(Solution().isPrintable([[1,1,1],[3,1,3]]))

    def test_isPrintable_4(self):
        self.assertFalse(Solution().isPrintable([[3,3,2,4,2],[3,2,4,3,3],[4,3,3,3,2],[2,3,3,2,2],[4,3,4,2,2],[2,4,4,3,3],[4,4,2,2,3],[4,4,4,2,2],[2,3,4,3,3]]))

    def test_isPrintable_5(self):
        self.assertTrue(Solution().isPrintable([[1,1,1,1,1,1,2,2,2],[3,3,3,3,1,1,2,2,2],[3,3,3,3,1,1,1,1,4],[3,3,3,3,1,1,6,1,4],[3,3,3,3,1,1,1,1,4],[3,3,3,3,5,5,5,5,4]]))