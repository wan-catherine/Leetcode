from unittest import TestCase
from problems.N396_Rotate_Function import Solution

class TestSolution(TestCase):
    def test_maxRotateFunction(self):
        self.assertEqual(36, Solution().maxRotateFunction([4, 3, 2, 6]))
