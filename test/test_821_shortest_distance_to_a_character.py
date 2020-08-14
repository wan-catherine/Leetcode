from unittest import TestCase
from problems.N821_Shortest_Distance_To_A_Character import Solution

class TestSolution(TestCase):
    def test_shortestToChar(self):
        output = [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
        self.assertListEqual(output, Solution().shortestToChar(S = "loveleetcode", C = 'e'))
