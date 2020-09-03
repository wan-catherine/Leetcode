from unittest import TestCase
from problems.N638_Shopping_Offers import Solution

class TestSolution(TestCase):
    def test_shoppingOffers(self):
        self.assertEqual(14, Solution().shoppingOffers([2,5], [[3,0,5],[1,2,10]], [3,2]))

    def test_shoppingOffers_1(self):
        self.assertEqual(11, Solution().shoppingOffers([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]))
