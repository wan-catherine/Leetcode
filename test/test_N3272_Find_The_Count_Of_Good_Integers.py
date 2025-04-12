from unittest import TestCase
from problems.N3272_Find_The_Count_Of_Good_Integers import Solution

class TestSolution(TestCase):
    def test_count_good_integers(self):
        self.assertEquals(27, Solution().countGoodIntegers(n = 3, k = 5))

    def test_count_good_integers_1(self):
        self.assertEquals(2, Solution().countGoodIntegers(n = 1, k = 4))

    def test_count_good_integers_2(self):
        self.assertEquals(2468, Solution().countGoodIntegers( n = 5, k = 6))
