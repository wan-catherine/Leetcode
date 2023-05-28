from unittest import TestCase
from problems.N2601_Prime_Subtraction_Operation import Solution

class TestSolution(TestCase):
    def test_prime_sub_operation(self):
        self.assertTrue(Solution().primeSubOperation([4,9,6,10]))

    def test_prime_sub_operation_1(self):
        self.assertTrue(Solution().primeSubOperation([6,8,11,12]))

    def test_prime_sub_operation_2(self):
        self.assertFalse(Solution().primeSubOperation([5,8,3]))

    def test_prime_sub_operation_3(self):
        self.assertFalse(Solution().primeSubOperation([1,20,7,12,4]))