from unittest import TestCase
from problems.N2827_Number_Of_Beautiful_Integers_In_The_Range import Solution

class TestSolution(TestCase):
    def test_number_of_beautiful_integers(self):
        self.assertEquals(2, Solution().numberOfBeautifulIntegers(low = 10, high = 20, k = 3))

    def test_number_of_beautiful_integers_1(self):
        self.assertEquals(1, Solution().numberOfBeautifulIntegers(low = 1, high = 10, k = 1))

    def test_number_of_beautiful_integers_2(self):
        self.assertEquals(0, Solution().numberOfBeautifulIntegers(low = 5, high = 5, k = 2))

    def test_number_of_beautiful_integers_3(self):
        self.assertEquals(3, Solution().numberOfBeautifulIntegers(low = 47, high = 100, k = 18))
