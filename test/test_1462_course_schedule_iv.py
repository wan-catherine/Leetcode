from unittest import TestCase
from problems.N1462_Course_Schedule_IV import Solution
false = False
true = True
class TestSolution(TestCase):
    def test_checkIfPrerequisite(self):
        self.assertListEqual([false,true], Solution().checkIfPrerequisite(n = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]))

    def test_checkIfPrerequisite_1(self):
        self.assertListEqual([false,false], Solution().checkIfPrerequisite(n = 2, prerequisites = [], queries = [[1,0],[0,1]]))

    def test_checkIfPrerequisite_2(self):
        self.assertListEqual([true,true], Solution().checkIfPrerequisite(n = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]))

    def test_checkIfPrerequisite_3(self):
        self.assertListEqual([false,true], Solution().checkIfPrerequisite(n = 3, prerequisites = [[1,0],[2,0]], queries = [[0,1],[2,0]]))

    def test_checkIfPrerequisite_4(self):
        self.assertListEqual([true,false,true,false], Solution().checkIfPrerequisite(n = 5, prerequisites = [[0,1],[1,2],[2,3],[3,4]], queries = [[0,4],[4,0],[1,3],[3,0]]))

