from unittest import TestCase
from problems.AddBinary import Solution

class TestSolution(TestCase):
    def test_addBinary(self):
        solution = Solution()
        res = solution.addBinary("11","1")
        self.assertEqual(res,"100")

    def test_addBinary_4(self):
        solution = Solution()
        res = solution.addBinary("1010","1011")
        self.assertEqual(res,"10101")

    def test_addBinary_1(self):
        solution = Solution()
        res = solution.addBinary("110010", "10111")
        self.assertEqual(res,"1001001")

