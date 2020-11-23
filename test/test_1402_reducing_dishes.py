from unittest import TestCase
from problems.N1402_Reducing_Dishes import Solution

class TestSolution(TestCase):
    def test_maxSatisfaction(self):
        self.assertEqual(14, Solution().maxSatisfaction([-1,-8,0,5,-9]))

    def test_maxSatisfaction_1(self):
        self.assertEqual(20, Solution().maxSatisfaction([4,3,2]))

    def test_maxSatisfaction_2(self):
        self.assertEqual(0, Solution().maxSatisfaction([-1,-4,-5]))

    def test_maxSatisfaction_3(self):
        self.assertEqual(35, Solution().maxSatisfaction([-2,5,-1,0,3,-3]))
