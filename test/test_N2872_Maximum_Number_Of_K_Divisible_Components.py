from unittest import TestCase
from problems.N2872_Maximum_Number_Of_K_Divisible_Components import Solution

class TestSolution(TestCase):
    def test_max_kdivisible_components(self):
        self.assertEquals(2, Solution().maxKDivisibleComponents(n = 5, edges = [[0,2],[1,2],[1,3],[2,4]], values = [1,8,1,4,4], k = 6))

    def test_max_kdivisible_components_1(self):
        self.assertEquals(3, Solution().maxKDivisibleComponents(n = 7, edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [3,0,6,1,5,2,1], k = 3))
