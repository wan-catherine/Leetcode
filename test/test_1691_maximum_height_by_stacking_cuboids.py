from unittest import TestCase
from problems.N1691_Maximum_Height_By_Stacking_Cuboids import Solution

class TestSolution(TestCase):
    def test_maxHeight(self):
        self.assertEqual(190, Solution().maxHeight([[50,45,20],[95,37,53],[45,23,12]]))

    def test_maxHeight_1(self):
        self.assertEqual(76, Solution().maxHeight([[38,25,45],[76,35,3]]))

    def test_maxHeight_2(self):
        self.assertEqual(102, Solution().maxHeight([[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]))
