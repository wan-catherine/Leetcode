from unittest import TestCase
from problems.N1388_Pizza_With_3n_Slices import Solution

class TestSolution(TestCase):
    def test_maxSizeSlices(self):
        self.assertEqual(10, Solution().maxSizeSlices([1,2,3,4,5,6]))

    def test_maxSizeSlices_1(self):
        self.assertEqual(16, Solution().maxSizeSlices([8,9,8,6,1,1]))

    def test_maxSizeSlices_2(self):
        self.assertEqual(21, Solution().maxSizeSlices([4,1,2,5,8,3,1,9,7]))

    def test_maxSizeSlices_3(self):
        self.assertEqual(3, Solution().maxSizeSlices([3,1,2]))
