from unittest import TestCase
from problems.N649_Dota2_Senate import Solution

class TestSolution(TestCase):
    def test_predictPartyVictory(self):
        self.assertEqual("Radiant", Solution().predictPartyVictory("RD"))

    def test_predictPartyVictory_1(self):
        self.assertEqual("Dire", Solution().predictPartyVictory("RDD"))

    def test_predictPartyVictory_2(self):
        self.assertEqual("Dire", Solution().predictPartyVictory("DDRRR"))

    def test_predictPartyVictory_3(self):
        self.assertEqual("Dire", Solution().predictPartyVictory("D"))
