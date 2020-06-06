from unittest import TestCase
from problems.N406_Queue_Reconstruction_By_Height import Solution

class TestSolution(TestCase):
    def test_reconstructQueue(self):
        input = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
        output = [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
        self.assertListEqual(output, Solution().reconstructQueue(input))