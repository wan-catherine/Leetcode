from unittest import TestCase
from problems.N1452_People_Whose_List_Of_Favorite_Companies_Is_Not_A_Subset_Of_Another_List import Solution

class TestSolution(TestCase):
    def test_peopleIndexes(self):
        self.assertListEqual([0,1,4], Solution().peopleIndexes([["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]))

    def test_peopleIndexes_1(self):
        self.assertListEqual([0,1], Solution().peopleIndexes([["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]))

    def test_peopleIndexes_2(self):
        self.assertListEqual([0,1,2,3], Solution().peopleIndexes([["leetcode"],["google"],["facebook"],["amazon"]]))