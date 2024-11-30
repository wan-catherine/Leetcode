from unittest import TestCase
from problems.N2097_Valid_Arrangement_Of_Pairs import Solution

class TestSolution(TestCase):
    def test_valid_arrangement(self):
        self.assertListEqual([[11,9],[9,4],[4,5],[5,1]], Solution().validArrangement([[5,1],[4,5],[11,9],[9,4]]))

    def test_valid_arrangement_1(self):
        self.assertListEqual([[1,3],[3,2],[2,1]], Solution().validArrangement([[1,3],[3,2],[2,1]]))

    def test_valid_arrangement_2(self):
        self.assertListEqual([[1,2],[2,1],[1,3]], Solution().validArrangement([[1,2],[1,3],[2,1]]))
