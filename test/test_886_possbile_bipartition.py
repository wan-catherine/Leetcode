from unittest import TestCase
from problems.N886_Possible_Bipartition import Solution

class TestSolution(TestCase):
    def test_possibleBipartition(self):
        self.assertTrue(Solution().possibleBipartition(4, [[1,2],[1,3],[2,4]]))

    def test_possibleBipartition_1(self):
        self.assertFalse(Solution().possibleBipartition(3, [[1,2],[1,3],[2,3]]))

    def test_possibleBipartition_2(self):
        self.assertFalse(Solution().possibleBipartition(5, [[1,2],[2,3],[3,4],[4,5],[1,5]]))
