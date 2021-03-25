from unittest import TestCase
from problems.N546_Remove_Boxes import Solution

class TestSolution(TestCase):
    def test_remove_boxes(self):
        self.assertEqual(23, Solution().removeBoxes([1,3,2,2,2,3,4,3,1]))

    def test_remove_boxes_1(self):
        self.assertEqual(9, Solution().removeBoxes([1,1,1]))

    def test_remove_boxes_2(self):
        self.assertEqual(1, Solution().removeBoxes([1]))
