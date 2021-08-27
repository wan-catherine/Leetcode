from unittest import TestCase
from problems.N749_Contain_Virus import Solution

class TestSolution(TestCase):
    def test_contain_virus(self):
        self.assertEqual(10, Solution().containVirus([[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]))

    def test_contain_virus_1(self):
        self.assertEqual(4, Solution().containVirus([[1,1,1],[1,0,1],[1,1,1]]))

    def test_contain_virus_2(self):
        self.assertEqual(13, Solution().containVirus([[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]))