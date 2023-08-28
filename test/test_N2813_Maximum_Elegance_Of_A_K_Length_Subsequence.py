from unittest import TestCase
from problems.N2813_Maximum_Elegance_Of_A_K_Length_Subsequence import Solution

class TestSolution(TestCase):
    def test_find_maximum_elegance(self):
        self.assertEquals(17, Solution().findMaximumElegance(items = [[3,2],[5,1],[10,1]], k = 2))

    def test_find_maximum_elegance_1(self):
        self.assertEquals(19, Solution().findMaximumElegance(items = [[3,1],[3,1],[2,2],[5,3]], k = 3))

    def test_find_maximum_elegance_2(self):
        self.assertEquals(7, Solution().findMaximumElegance(items = [[1,1],[2,1],[3,1]], k = 3))

    def test_find_maximum_elegance_3(self):
        self.assertEquals(24, Solution().findMaximumElegance(items = [[7,1],[4,1],[3,2],[10,1]], k = 3))

    def test_find_maximum_elegance_4(self):
        self.assertEquals(51, Solution().findMaximumElegance(items = [[1,6],[10,1],[4,4],[8,1],[6,2],[10,1],[5,5],[4,4]], k = 5))
