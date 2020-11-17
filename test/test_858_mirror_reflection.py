from unittest import TestCase
from problems.N858_Mirror_Reflection import Solution

class TestSolution(TestCase):
    def test_mirrorReflection(self):
        self.assertEqual(2, Solution().mirrorReflection(2,1))
