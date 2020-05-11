from unittest import TestCase
from problems.N997_Find_The_Town_Judge import Solution

class TestSolution(TestCase):
    def test_findJudge(self):
        self.assertEqual(2, Solution().findJudge(2, [[1,2]]))

    def test_findJudge_1(self):
        self.assertEqual(3, Solution().findJudge(3, [[1,3],[2,3]]))

    def test_findJudge_2(self):
        self.assertEqual(-1, Solution().findJudge(3, [[1,3],[2,3],[3,1]]))

    def test_findJudge_3(self):
        self.assertEqual(-1, Solution().findJudge(3, [[1,2],[2,3]]))

    def test_findJudge_4(self):
        self.assertEqual(3, Solution().findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))

    def test_findJudge_5(self):
        self.assertEqual(1, Solution().findJudge(1, []))

    def test_findJudge_6(self):
        self.assertEqual(-1, Solution().findJudge(11, [[1,8],[1,3],[2,8],[2,3],[4,8],[4,3],[5,8],[5,3],[6,8],[6,3],[7,8],[7,3],[9,8],[9,3],[11,8],[11,3]]))

