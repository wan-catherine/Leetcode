from unittest import TestCase
from problems.N839_Similar_String_Groups import Solution

class TestSolution(TestCase):
    def test_numSimilarGroups(self):
        self.assertEqual(2, Solution().numSimilarGroups(["tars","rats","arts","star"]))

    def test_numSimilarGroups_1(self):
        self.assertEqual(1, Solution().numSimilarGroups(["omv","ovm"]))
