from unittest import TestCase
from problems.N1345_Jump_Game_IV import Solution

class TestSolution(TestCase):
    def test_minJumps(self):
        self.assertEqual(3, Solution().minJumps([100,-23,-23,404,100,23,23,23,3,404]))

    def test_minJumps_1(self):
        self.assertEqual(0, Solution().minJumps([7]))

    def test_minJumps_2(self):
        self.assertEqual(1, Solution().minJumps([7,6,9,6,9,6,9,7]))

    def test_minJumps_3(self):
        self.assertEqual(2, Solution().minJumps([6,1,9]))

    def test_minJumps_4(self):
        self.assertEqual(3, Solution().minJumps([11,22,7,7,7,7,7,7,7,22,13]))
