from unittest import TestCase
from problems.N2440_Create_Components_With_Same_Value import Solution

class TestSolution(TestCase):
    def test_component_value(self):
        self.assertEqual(2, Solution().componentValue(nums = [6,2,2,2,6], edges = [[0,1],[1,2],[1,3],[3,4]]))

    def test_component_value_1(self):
        self.assertEqual(0, Solution().componentValue(nums = [2], edges = []))

    def test_component_value_2(self):
        self.assertEqual(1, Solution().componentValue([1,2,1,1,1], [[0,1],[1,3],[3,4],[4,2]]))

    def test_component_value_3(self):
        self.assertEqual(0, Solution().componentValue([1,1,2,1,1], [[0,2],[1,2],[3,2],[4,2]]))