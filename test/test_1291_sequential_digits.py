from unittest import TestCase
from problems.N1291_Sequential_Digits import Solution

class TestSolution(TestCase):
    def test_sequentialDigits(self):
        self.assertListEqual([123,234], Solution().sequentialDigits(low = 100, high = 300))

    def test_sequentialDigits_1(self):
        self.assertListEqual([1234,2345,3456,4567,5678,6789,12345], Solution().sequentialDigits(low = 1000, high = 13000))

    def test_sequentialDigits_2(self):
        self.assertListEqual([12,23,34,45,56,67,78,89,123,234,345,456,567,678,789,1234,2345,3456,4567,5678,6789,12345,23456,34567,45678,56789,123456,234567,345678,456789,1234567,2345678,3456789,12345678,23456789,123456789], Solution().sequentialDigits(10, 1000000000))

    def test_sequentialDigits_3(self):
        self.assertListEqual([67,78,89,123], Solution().sequentialDigits(58, 155))