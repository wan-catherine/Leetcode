from unittest import TestCase
from problems.N1029_Two_City_Scheduling import Solution

class TestSolution(TestCase):
    def test_twoCitySchedCost(self):
        self.assertEqual(110, Solution().twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))
