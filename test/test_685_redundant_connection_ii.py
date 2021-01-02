from unittest import TestCase
from problems.N685_Redundant_Connection_II import Solution

class TestSolution(TestCase):
    def test_findRedundantDirectedConnection(self):
        self.assertListEqual([2,3], Solution().findRedundantDirectedConnection([[1,2],[1,3],[2,3]]))

    def test_findRedundantDirectedConnection_1(self):
        self.assertListEqual([4,1], Solution().findRedundantDirectedConnection([[1,2],[2,3],[3,4],[4,1],[1,5]]))
