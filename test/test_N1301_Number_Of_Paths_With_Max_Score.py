from unittest import TestCase
from problems.N1301_Number_Of_Paths_With_Max_Score import Solution

class TestSolution(TestCase):
    def test_paths_with_max_score(self):
        self.assertListEqual([7,1], Solution().pathsWithMaxScore(["E23","2X2","12S"]))

    def test_paths_with_max_score_1(self):
        self.assertListEqual([4,2], Solution().pathsWithMaxScore(["E12","1X1","21S"]))

    def test_paths_with_max_score_2(self):
        self.assertListEqual([0,0], Solution().pathsWithMaxScore(["E11","XXX","11S"]))

