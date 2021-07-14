from unittest import TestCase
from problems.N1901_Find_A_Peak_Element_II import Solution

class TestSolution(TestCase):
    def test_find_peak_grid(self):
        self.assertListEqual([0,1], Solution().findPeakGrid([[1,4],[3,2]]))

    def test_find_peak_grid_1(self):
        self.assertListEqual([1,1], Solution().findPeakGrid([[10,20,15],[21,30,14],[7,16,32]]))

    def test_find_peak_grid_2(self):
        self.assertListEqual([2,0], Solution().findPeakGrid([[41,8,2,48,18],[16,15,9,7,44],[48,35,6,38,28],[3,2,14,15,33],[39,36,13,46,42]]))

    def test_find_peak_grid_3(self):
        self.assertListEqual([0,2], Solution().findPeakGrid([[1,2,6],[3,4,5]]))

    def test_find_peak_grid_4(self):
        self.assertListEqual([0,0], Solution().findPeakGrid([[7,2,3,1,2],[6,5,4,2,1]]))

    def test_find_peak_grid_5(self):
        self.assertListEqual([0,0], Solution().findPeakGrid([[10,30,40,50,20],[1,3,2,500,4]]))
