from unittest import TestCase
from problems.N2861_Maximum_Number_Of_Alloys import Solution


class TestSolution(TestCase):
    def test_max_number_of_alloys(self):
        self.assertEqual(2, Solution().maxNumberOfAlloys(n = 3, k = 2, budget = 15, composition = [[1,1,1],[1,1,10]], stock = [0,0,0], cost = [1,2,3]))

    def test_max_number_of_alloys_1(self):
        self.assertEqual(5, Solution().maxNumberOfAlloys(n = 3, k = 2, budget = 15, composition = [[1,1,1],[1,1,10]], stock = [0,0,100], cost = [1,2,3]))

    def test_max_number_of_alloys_2(self):
        self.assertEqual(2, Solution().maxNumberOfAlloys(n = 2, k = 3, budget = 10, composition = [[2,1],[1,2],[1,1]], stock = [1,1], cost = [5,5]))

    def test_max_number_of_alloys_3(self):
        self.assertEqual(54, Solution().maxNumberOfAlloys(n = 1, k = 7, budget = 48, composition = [[1],[5],[9],[6],[4],[2],[4]], stock = [6], cost = [1]))
