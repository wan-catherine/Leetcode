from unittest import TestCase
from problems.N2954_Count_The_Number_Of_Infection_Sequences import Solution

class TestSolution(TestCase):
    def test_number_of_sequence(self):
        self.assertEquals(4, Solution().numberOfSequence(n = 5, sick = [0,4]))

    def test_number_of_sequence_1(self):
        self.assertEquals(3, Solution().numberOfSequence(n = 4, sick = [1]))
