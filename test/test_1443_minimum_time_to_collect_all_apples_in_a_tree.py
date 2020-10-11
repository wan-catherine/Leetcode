from unittest import TestCase
from problems.N1443_Minimum_Time_To_Collect_All_Apples_In_A_Tree import Solution
false = False
true = True
class TestSolution(TestCase):
    def test_minTime(self):
        self.assertEqual(8, Solution().minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]))

    def test_minTime_1(self):
        self.assertEqual(6, Solution().minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]))

    def test_minTime_2(self):
        self.assertEqual(0, Solution().minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]))
