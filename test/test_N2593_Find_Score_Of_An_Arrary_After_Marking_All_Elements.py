from unittest import TestCase
from problems.N2593_Find_Score_Of_An_Arrary_After_Marking_All_Elements import Solution

class TestSolution(TestCase):
    def test_find_score(self):
        self.assertEqual(5, Solution().findScore([2,3,5,1,3,2]))

    def test_find_score_1(self):
        self.assertEqual(212, Solution().findScore([10,44,10,8,48,30,17,38,41,27,16,33,45,45,34,30,22,3,42,42]))

