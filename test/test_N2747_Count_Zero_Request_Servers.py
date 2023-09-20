from unittest import TestCase
from problems.N2747_Count_Zero_Request_Servers import Solution

class TestSolution(TestCase):
    def test_count_servers(self):
        self.assertListEqual([1,2], Solution().countServers(n = 3, logs = [[1,3],[2,6],[1,5]], x = 5, queries = [10,11]))

    def test_count_servers_1(self):
        self.assertListEqual([0,1], Solution().countServers(n = 3, logs = [[2,4],[2,1],[1,2],[3,1]], x = 2, queries = [3,4]))

    def test_count_servers_2(self):
        self.assertListEqual([2,3,3,3], Solution().countServers(n = 4, logs = [[2,30],[2,5],[3,9],[4,21]], x = 9, queries = [11,28,16,18]))
