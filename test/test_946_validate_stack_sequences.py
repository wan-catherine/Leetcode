from unittest import TestCase
from problems.N946_Validate_Stack_Sequences import Solution

class TestSolution(TestCase):
    def test_validateStackSequences(self):
        self.assertTrue(Solution().validateStackSequences(pushed = [1,2,3,4,5], popped = [4,5,3,2,1]))

    def test_validateStackSequences_1(self):
        self.assertFalse(Solution().validateStackSequences(pushed = [1,2,3,4,5], popped = [4,3,5,1,2]))
