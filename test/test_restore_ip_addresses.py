from unittest import TestCase
from problems.RestoreIPAddresses import Solution

class TestSolution(TestCase):
    def test_restoreIpAddresses(self):
        solution = Solution()
        res = solution.restoreIpAddresses("25525511135")
        self.assertEqual(["255.255.11.135", "255.255.111.35"], res)

    def test_restoreIpAddresses_one(self):
        solution = Solution()
        res = solution.restoreIpAddresses("010010")
        self.assertEqual(["0.10.0.10","0.100.1.0"], res)

    def test_restoreIpAddresses_two(self):
        solution = Solution()
        res = solution.restoreIpAddresses("103574606193")
        self.assertEqual([], res)