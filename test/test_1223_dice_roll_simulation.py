from unittest import TestCase
from problems.N1223_Dice_Roll_Simulation import Solution

class TestSolution(TestCase):
    def test_dieSimulator(self):
        self.assertEqual(34, Solution().dieSimulator(n = 2, rollMax = [1,1,2,2,2,3]))

    def test_dieSimulator_1(self):
        self.assertEqual(30, Solution().dieSimulator(n = 2, rollMax = [1,1,1,1,1,1]))

    def test_dieSimulator_2(self):
        self.assertEqual(181, Solution().dieSimulator(n = 3, rollMax = [1,1,1,2,2,3]))

