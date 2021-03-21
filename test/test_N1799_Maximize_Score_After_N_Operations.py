from unittest import TestCase
from problems.N1799_Maximize_Score_After_N_Operations import Solution

class TestSolution(TestCase):
    def test_max_score(self):
        self.assertEqual(1, Solution().maxScore([1,2]))

    def test_max_score_1(self):
        self.assertEqual(11, Solution().maxScore([3,4,6,8]))

    def test_max_score_2(self):
        self.assertEqual(14, Solution().maxScore([1,2,3,4,5,6]))

    def test_max_score_3(self):
        self.assertEqual(40, Solution().maxScore([481851,31842,817070,452937,627635,712245]))
