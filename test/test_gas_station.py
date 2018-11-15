from unittest import TestCase
from problems.GasStation import Solution

class TestSolution(TestCase):
    def test_canCompleteCircuit(self):
        solution = Solution()
        res = solution.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])
        self.assertEqual(3, res)

    def test_canCompleteCircuit_one(self):
        solution = Solution()
        res = solution.canCompleteCircuit([2,3,4], [3,4,3])
        self.assertEqual(-1, res)

    def test_canCompleteCircuit_two(self):
        solution = Solution()
        res = solution.canCompleteCircuit([3,1,1], [1,2,2])
        self.assertEqual(0, res)
