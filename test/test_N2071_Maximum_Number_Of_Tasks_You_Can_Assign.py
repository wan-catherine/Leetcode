from unittest import TestCase
from problems.N2071_Maximum_Number_Of_Tasks_You_Can_Assign import Solution

class TestSolution(TestCase):
    def test_max_task_assign(self):
        self.assertEqual(3, Solution().maxTaskAssign(tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1))

    def test_max_task_assign_1(self):
        self.assertEqual(1, Solution().maxTaskAssign(tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5))

    def test_max_task_assign_2(self):
        self.assertEqual(2, Solution().maxTaskAssign(tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10))

    def test_max_task_assign_3(self):
        self.assertEqual(3, Solution().maxTaskAssign(tasks = [5,9,8,5,9], workers = [1,6,4,2,6], pills = 1, strength = 5))
