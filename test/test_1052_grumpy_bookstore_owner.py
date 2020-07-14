from unittest import TestCase
from problems.N1052_Grumpy_Bookstore_Owner import Solution

class TestSolution(TestCase):
    def test_maxSatisfied(self):
        customers = [1, 0, 1, 2, 1, 1, 7, 5]
        grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
        X = 3
        self.assertEqual(16, Solution().maxSatisfied(customers,grumpy, X))

    def test_maxSatisfied_1(self):
        customers = [6,10,2,1,7,9]
        grumpy = [1,0,0,0,0,1]
        X = 3
        self.assertEqual(29, Solution().maxSatisfied(customers,grumpy, X))