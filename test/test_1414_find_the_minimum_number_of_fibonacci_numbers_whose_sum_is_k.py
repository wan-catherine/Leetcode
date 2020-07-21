from unittest import TestCase
from problems.N1414_Find_The_Minimum_Number_Of_Fibonacci_Numbers_Whose_Sum_Is_K import Solution

class TestSolution(TestCase):
    def test_findMinFibonacciNumbers(self):
        self.assertEqual(2, Solution().findMinFibonacciNumbers(7))

    def test_findMinFibonacciNumbers_1(self):
        self.assertEqual(2, Solution().findMinFibonacciNumbers(10))

    def test_findMinFibonacciNumbers_2(self):
        self.assertEqual(3, Solution().findMinFibonacciNumbers(19))
