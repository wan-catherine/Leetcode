from unittest import TestCase
from problems.N2768_Number_Of_Black_Blocks import Solution

class TestSolution(TestCase):
    def test_count_black_blocks(self):
        self.assertListEqual([3,1,0,0,0], Solution().countBlackBlocks(m = 3, n = 3, coordinates = [[0,0]]))

    def test_count_black_blocks_1(self):
        self.assertListEqual([0,2,2,0,0], Solution().countBlackBlocks(m = 3, n = 3, coordinates = [[0,0],[1,1],[0,2]]))
