from unittest import TestCase
from problems.N881_Boats_To_Save_People import Solution

class TestSolution(TestCase):
    def test_numRescueBoats(self):
        self.assertEqual(1, Solution().numRescueBoats(people = [1,2], limit = 3))

    def test_numRescueBoats_1(self):
        self.assertEqual(3, Solution().numRescueBoats(people = [3,2,2,1], limit = 3))

    def test_numRescueBoats_2(self):
        self.assertEqual(4, Solution().numRescueBoats(people = [3,5,3,4], limit = 5))
