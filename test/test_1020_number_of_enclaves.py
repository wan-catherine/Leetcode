from unittest import TestCase
from problems.N1020_Number_Of_Enclaves import Solution

class TestSolution(TestCase):
    def test_numEnclaves(self):
        self.assertEqual(3, Solution().numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))

    def test_numEnclaves_1(self):
        self.assertEqual(0, Solution().numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]))

