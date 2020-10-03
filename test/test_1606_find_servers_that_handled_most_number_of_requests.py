from unittest import TestCase
from problems.N1606_Find_Servers_That_Handled_Most_Number_Of_Requests import Solution

class TestSolution(TestCase):
    def test_busiestServers(self):
        self.assertListEqual([1], Solution().busiestServers(k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3]))

    def test_busiestServers_1(self):
        self.assertListEqual([0], Solution().busiestServers(k = 3, arrival = [1,2,3,4], load = [1,2,1,2]))

    def test_busiestServers_2(self):
        self.assertListEqual([0,1,2], Solution().busiestServers(k = 3, arrival = [1,2,3], load = [10,12,11]))

    def test_busiestServers_3(self):
        self.assertListEqual([1], Solution().busiestServers(k = 3, arrival = [1,2,3,4,8,9,10], load = [5,2,10,3,1,2,2]))

    def test_busiestServers_4(self):
        self.assertListEqual([0], Solution().busiestServers(k = 1, arrival = [1], load = [1]))

    def test_busiestServers_5(self):
        self.assertListEqual([1], Solution().busiestServers(5, [1,2,4,5,7,9,11,12,13,15], [14,5,18,19,19,4,8,18,1,9]))