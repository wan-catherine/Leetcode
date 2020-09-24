from unittest import TestCase
from problems.N1155_Number_Of_Dice_Rolls_With_Target_Sum import Solution

class TestSolution(TestCase):
    def test_numRollsToTarget(self):
        self.assertEqual(1, Solution().numRollsToTarget(d = 1, f = 6, target = 3))

    def test_numRollsToTarget_1(self):
        self.assertEqual(6, Solution().numRollsToTarget(d = 2, f = 6, target = 7))

    def test_numRollsToTarget_2(self):
        self.assertEqual(1, Solution().numRollsToTarget(d = 2, f = 5, target = 10))

    def test_numRollsToTarget_3(self):
        self.assertEqual(0, Solution().numRollsToTarget(d = 1, f = 2, target = 3))

    def test_numRollsToTarget_4(self):
        self.assertEqual(222616187, Solution().numRollsToTarget(d = 30, f = 30, target = 500))
