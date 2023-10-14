from unittest import TestCase
from problems.N2896_Apply_Operations_To_Make_Two_Strings_Equal import Solution

class TestSolution(TestCase):
    def test_min_operations(self):
        self.assertEquals(4, Solution().minOperations(s1 = "1100011000", s2 = "0101001010", x = 2))

    def test_min_operations_1(self):
        self.assertEquals(-1, Solution().minOperations(s1 = "10110", s2 = "00011", x = 4))

    def test_min_operations_2(self):
        self.assertEquals(8, Solution().minOperations(s1 = "00101101100010", s2 = "00001010001111", x = 30))

    def test_min_operations_3(self):
        self.assertEquals(4, Solution().minOperations(s1 = "11001011111", s2 = "01111000110", x = 2))

