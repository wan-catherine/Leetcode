from unittest import TestCase
from problems.N2337_Move_Pieces_To_Obtain_A_String import Solution

class TestSolution(TestCase):
    def test_can_change(self):
        self.assertTrue(Solution().canChange(start = "_L__R__R_", target = "L______RR"))

    def test_can_change_1(self):
        self.assertFalse(Solution().canChange(start = "R_L_", target = "__LR"))

    def test_can_change_2(self):
        self.assertFalse(Solution().canChange(start = "_R", target = "R_"))