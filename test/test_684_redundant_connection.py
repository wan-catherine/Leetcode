from unittest import TestCase
from problems.N684_Redundant_Connection import Solution

class TestSolution(TestCase):
    def test_findRedundantConnection(self):
        self.assertListEqual([2,3], Solution().findRedundantConnection([[1,2], [1,3], [2,3]]))

    def test_findRedundantConnection_1(self):
        self.assertListEqual([1,4], Solution().findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))

    def test_findRedundantConnection_2(self):
        self.assertListEqual([1,3], Solution().findRedundantConnection([[1,4],[3,4],[1,3],[1,2],[4,5]]))
