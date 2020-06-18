from unittest import TestCase
from problems.N621_Task_Scheduler import Solution

class TestSolution(TestCase):
    def test_leastInterval(self):
        self.assertEqual(8, Solution().leastInterval(["A","A","A","B","B","B"], 2))

    def test_leastInterval_1(self):
        self.assertEqual(52, Solution().leastInterval(["A","A","B","B","C","C","D","D","E","E","F","F","G","G","H","H","I","I","J","J","K","K","L","L","M","M","N","N","O","O","P","P","Q","Q","R","R","S","S","T","T","U","U","V","V","W","W","X","X","Y","Y","Z","Z"], 2))

    def test_leastInterval_2(self):
        self.assertEqual(16, Solution().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"],2))