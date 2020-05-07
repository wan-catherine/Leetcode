from unittest import TestCase
from problems.BulbSwitcher import Solution

class TestSolution(TestCase):
    def test_bulbSwitch(self):
        solution = Solution()
        res = solution.bulbSwitch(3)
        self.assertEqual(1, res)
