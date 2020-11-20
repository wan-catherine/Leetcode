from unittest import TestCase
from problems.N1349_Maximum_Students_Taking_Exam import Solution

class TestSolution(TestCase):
    def test_maxStudents(self):
        seats = [["#",".","#","#",".","#"],
                [".","#","#","#","#","."],
                ["#",".","#","#",".","#"]]
        self.assertEqual(4, Solution().maxStudents(seats))

    def test_maxStudents_1(self):
        seats = [[".","#"],
                ["#","#"],
                ["#","."],
                ["#","#"],
                [".","#"]]
        self.assertEqual(3, Solution().maxStudents(seats))

    def test_maxStudents_2(self):
        seats = [["#",".",".",".","#"],
                [".","#",".","#","."],
                [".",".","#",".","."],
                [".","#",".","#","."],
                ["#",".",".",".","#"]]
        self.assertEqual(10, Solution().maxStudents(seats))