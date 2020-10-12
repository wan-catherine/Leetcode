from unittest import TestCase
from problems.N802_Find_Eventual_Safe_States import Solution

class TestSolution(TestCase):
    def test_eventualSafeNodes(self):
        self.assertListEqual([2,4,5,6], Solution().eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))
