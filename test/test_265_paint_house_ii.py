from unittest import TestCase
from problems.N265_Paint_House_II import Solution

class TestSolution(TestCase):
    def test_minCostII(self):
        self.assertEqual(5, Solution().minCostII([[1,5,3],[2,9,4]]))

    def test_minCostII_1(self):
        self.assertEqual(9, Solution().minCostII([[3,14,12,2,20,16,12,2],[9,6,9,8,2,9,20,18],[20,2,20,4,5,12,11,11],[16,3,7,5,15,2,2,4],[17,3,11,1,9,5,7,11]]))

    def test_minCostII_2(self):
        self.assertEqual(230, Solution().minCostII([[1,2],[1,19],[17,13],[3,20],[20,16],[9,8],[2,7],[19,18],[14,1],[16,20],[5,8],[10,10],[1,15],[15,6],[16,13],[17,2],[11,16],[6,13],[5,7],[17,5],[16,13],[19,1]]))