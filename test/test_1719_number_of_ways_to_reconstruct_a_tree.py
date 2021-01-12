from unittest import TestCase
from problems.N1719_Number_Of_Ways_To_Reconstruct_A_Tree import Solution

class TestSolution(TestCase):
    def test_checkWays(self):
        self.assertEqual(1, Solution().checkWays([[1,2],[2,3]]))

    def test_checkWays_1(self):
        self.assertEqual(2, Solution().checkWays([[1,2],[2,3],[1,3]]))

    def test_checkWays_2(self):
        self.assertEqual(0, Solution().checkWays([[1,2],[2,3],[2,4],[1,5]]))

    def test_checkWays_3(self):
        self.assertEqual(1, Solution().checkWays([[3,5],[4,5],[2,5],[1,5],[1,4],[2,4]]))

    def test_checkWays_4(self):
        self.assertEqual(2, Solution().checkWays([[1,5],[1,3],[2,3],[2,4],[3,5],[3,4]]))

    def test_checkWays_5(self):
        self.assertEqual(1, Solution().checkWays([[11,13],[2,11],[8,12],[7,9],[7,15],[4,14],[1,14],[8,11],[3,5],[8,9],[14,15],[3,14],[2,8],[4,9],[13,14],[12,14],[6,14],[9,14],[4,8],[9,12],[5,11],[6,9],[3,13],[5,9],[3,9],[2,9],[3,4],[3,12],[9,13],[2,13],[8,14],[8,13],[11,12],[5,14],[9,15],[11,14],[6,15],[7,14],[3,8],[9,11],[2,14],[3,11],[9,10],[1,9],[1,8],[2,3],[5,8],[2,5]]))

    def test_checkWays_6(self):
        self.assertEqual(2, Solution().checkWays([[1,2]]))