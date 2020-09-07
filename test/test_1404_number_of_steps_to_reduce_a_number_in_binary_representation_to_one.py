from unittest import TestCase
from problems.N1404_Number_Of_Steps_To_Reduce_A_Number_In_Binary_Representation_To_One import Solution

class TestSolution(TestCase):
    def test_numSteps(self):
        self.assertEqual(6, Solution().numSteps("1101"))

    def test_numSteps_1(self):
        self.assertEqual(1, Solution().numSteps("10"))

    def test_numSteps(self):
        self.assertEqual(0, Solution().numSteps("1"))
