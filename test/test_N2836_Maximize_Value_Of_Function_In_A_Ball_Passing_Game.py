from unittest import TestCase
from problems.N2836_Maximize_Value_Of_Function_In_A_Ball_Passing_Game import Solution

class TestSolution(TestCase):
    def test_get_max_function_value(self):
        self.assertEquals(6, Solution().getMaxFunctionValue(receiver = [2,0,1], k = 4))

    def test_get_max_function_value_1(self):
        self.assertEquals(10, Solution().getMaxFunctionValue(receiver = [1,1,1,2,3], k = 3))
