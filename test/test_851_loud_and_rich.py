from unittest import TestCase
from problems.N851_Loud_And_Rich import Solution

class TestSolution(TestCase):
    def test_loudAndRich(self):
        self.assertListEqual([5,5,2,5,4,5,6,7], Solution().loudAndRich(richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]))
