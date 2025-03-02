from unittest import TestCase
from problems.N2106_Maximum_Fruits_Harvested_After_At_Most_K_Steps import Solution

class TestSolution(TestCase):
    def test_max_total_fruits(self):
        self.assertEquals(9, Solution().maxTotalFruits(fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4))

    def test_max_total_fruits_1(self):
        self.assertEquals(14, Solution().maxTotalFruits(fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4))

    def test_max_total_fruits_2(self):
        self.assertEquals(0, Solution().maxTotalFruits(fruits = [[0,3],[6,4],[8,5]], startPos = 3, k = 2))

    def test_max_total_fruits_3(self):
        self.assertEquals(10000, Solution().maxTotalFruits(fruits = [[0,10000]], startPos = 200000, k = 200000))
