from unittest import TestCase
from problems.N2517_Maximum_Tastiness_Of_Candy_Basket import Solution

class TestSolution(TestCase):
    def test_maximum_tastiness(self):
        self.assertEqual(8, Solution().maximumTastiness(price = [13,5,1,8,21,2], k = 3))

    def test_maximum_tastiness_1(self):
        self.assertEqual(2, Solution().maximumTastiness(price = [1,3,1], k = 2))

    def test_maximum_tastiness_2(self):
        self.assertEqual(0, Solution().maximumTastiness(price = [7,7,7,7], k = 2))

    def test_maximum_tastiness_3(self):
        self.assertEqual(19, Solution().maximumTastiness(price = [34,116,83,15,150,56,69,42,26], k = 6))
