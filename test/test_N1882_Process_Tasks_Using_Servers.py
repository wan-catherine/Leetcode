from unittest import TestCase
from problems.N1882_Process_Tasks_Using_Servers import Solution

class TestSolution(TestCase):
    def test_assign_tasks(self):
        self.assertListEqual([2,2,0,2,1,2], Solution().assignTasks(servers = [3,3,2], tasks = [1,2,3,2,1,2]))

    def test_assign_tasks_1(self):
        self.assertListEqual([1,4,1,4,1,3,2], Solution().assignTasks(servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]))
