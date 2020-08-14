from unittest import TestCase
from problems.N838_Push_Dominoes import Solution

class TestSolution(TestCase):
    def test_pushDominoes(self):
        self.assertEqual("LL.RR.LLRRLL..", Solution().pushDominoes(".L.R...LR..L.."))

    def test_pushDominoes_1(self):
        self.assertEqual("RR.L", Solution().pushDominoes("RR.L"))

    def test_pushDominoes_2(self):
        self.assertEqual("LL.RR", Solution().pushDominoes(".L.R."))

    def test_pushDominoes_3(self):
        self.assertEqual("L", Solution().pushDominoes("L"))

    def test_pushDominoes_4(self):
        self.assertEqual("LL", Solution().pushDominoes(".L"))

    def test_pushDominoes_5(self):
        self.assertEqual("RR", Solution().pushDominoes("RR"))

    def test_pushDominoes_6(self):
        self.assertEqual("RRR.L", Solution().pushDominoes("R.R.L"))

    def test_pushDominoes_7(self):
        self.assertEqual("RRRRRRL...", Solution().pushDominoes("RRRRRRL..."))
