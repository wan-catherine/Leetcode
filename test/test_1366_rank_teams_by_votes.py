from unittest import TestCase
from problems.N1366_Rank_Teams_By_Votes import Solution

class TestSolution(TestCase):
    def test_rankTeams(self):
        self.assertEqual("ACB", Solution().rankTeams(["ABC","ACB","ABC","ACB","ACB"]))

    def test_rankTeams_1(self):
        self.assertEqual("XWYZ", Solution().rankTeams(["WXYZ","XYZW"]))

    def test_rankTeams_2(self):
        self.assertEqual("ZMNAGUEDSJYLBOPHRQICWFXTVK", Solution().rankTeams(["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))

    def test_rankTeams_3(self):
        self.assertEqual("ABC", Solution().rankTeams(["BCA","CAB","CBA","ABC","ACB","BAC"]))

    def test_rankTeams_4(self):
        self.assertEqual("M", Solution().rankTeams(["M","M","M","M"]))
