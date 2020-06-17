from unittest import TestCase
from problems.N611_Valid_Triangle_Number import Solution

class TestSolution(TestCase):
    def test_triangleNumber(self):
        self.assertEqual(3, Solution().triangleNumber([2,2,3,4]))

    def test_triangleNumber_1(self):
        self.assertEqual(1, Solution().triangleNumber([0,1,1,1]))
