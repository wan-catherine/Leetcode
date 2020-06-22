from unittest import TestCase
from problems.N1222_Queens_That_Can_Attack_The_King import Solution

class TestSolution(TestCase):
    def test_queensAttacktheKing(self):
        queens = [[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]]
        king = [0, 0]
        self.assertListEqual(sorted([[0,1],[1,0],[3,3]]), Solution().queensAttacktheKing(queens, king))

    def test_queensAttacktheKing_1(self):
        queens = [[0, 0], [1, 1], [2, 2], [3, 4], [3, 5], [4, 4], [4, 5]]
        king = [3, 3]
        self.assertListEqual(sorted([[2,2],[3,4],[4,4]]), Solution().queensAttacktheKing(queens, king))

    def test_queensAttacktheKing_2(self):
        queens = [[5, 6], [7, 7], [2, 1], [0, 7], [1, 6], [5, 1], [3, 7], [0, 3], [4, 0], [1, 2], [6, 3], [5, 0],
                  [0, 4], [2, 2], [1, 1], [6, 4], [5, 4], [0, 0], [2, 6], [4, 5], [5, 2], [1, 4], [7, 5], [2, 3],
                  [0, 5], [4, 2], [1, 0], [2, 7], [0, 1], [4, 6], [6, 1], [0, 6], [4, 3], [1, 7]]
        king = [3, 4]
        self.assertListEqual(sorted([[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]), Solution().queensAttacktheKing(queens, king))

    def test_queensAttacktheKing_3(self):
        queens = [[4,7],[1,3],[6,6],[3,0],[0,2],[0,7],[6,2],[3,7],[5,1],[2,5],[0,3],[7,2],[4,0],[1,2],[3,3],[5,5],[4,4],[6,3],[1,5],[5,0],[0,4],[6,4],[5,4],[3,2],[0,0],[4,5],[0,5],[2,3],[1,0],[6,5],[5,3],[0,1],[7,0],[4,6],[5,7],[7,4],[2,0],[4,3],[3,4]]
        king = [2,4]
        self.assertListEqual(sorted([[1,3],[0,4],[1,5],[2,3],[2,5],[3,3],[3,4],[4,6]]), Solution().queensAttacktheKing(queens, king))

    def test_queensAttacktheKing_4(self):
        queens =[[7,3],[1,3],[6,6],[7,7],[0,7],[6,2],[1,6],[5,1],[2,5],[7,2],[6,7],[3,3],[5,5],[7,6],[6,3],[1,5],[3,6],[4,1],[6,4],[3,2],[0,0],[2,6],[7,1],[6,0],[1,4],[7,5],[1,0],[6,5],[5,3],[2,7],[3,5],[7,0],[4,6],[3,1],[7,4],[0,6],[2,0]]
        king = [4,3]
        self.assertListEqual(sorted([[3,2],[3,3],[2,5],[4,1],[4,6],[7,0],[5,3],[6,5]]), Solution().queensAttacktheKing(queens, king))