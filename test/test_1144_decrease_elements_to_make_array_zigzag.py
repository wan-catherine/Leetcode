from unittest import TestCase
from problems.N1144_Decrease_Elements_To_Make_Array_Zigzag import Solution

class TestSolution(TestCase):
    def test_movesToMakeZigzag(self):
        self.assertEqual(2, Solution().movesToMakeZigzag([1,2,3]))

    def test_movesToMakeZigzag_1(self):
        self.assertEqual(4, Solution().movesToMakeZigzag([9,6,1,6,2]))

    def test_movesToMakeZigzag_2(self):
        self.assertEqual(0, Solution().movesToMakeZigzag([2,1,2]))
