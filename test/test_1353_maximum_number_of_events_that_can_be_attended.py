from unittest import TestCase
from problems.N1353_Maximum_Number_Of_Events_That_Can_Be_Attended import Solution

class TestSolution(TestCase):
    def test_maxEvents(self):
        self.assertEqual(3, Solution().maxEvents([[1,2],[2,3],[3,4]]))

    def test_maxEvents_1(self):
        self.assertEqual(4, Solution().maxEvents([[1,2],[2,3],[3,4],[1,2]]))

    def test_maxEvents_2(self):
        self.assertEqual(4, Solution().maxEvents([[1,4],[4,4],[2,2],[3,4],[1,1]]))

    def test_maxEvents_3(self):
        self.assertEqual(1, Solution().maxEvents([[1,100000]]))

    def test_maxEvents_4(self):
        self.assertEqual(7, Solution().maxEvents([[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]))

    def test_maxEvents_5(self):
        self.assertEqual(5, Solution().maxEvents([[1,2],[1,2],[3,3],[1,5],[1,5]]))

    def test_maxEvents_6(self):
        self.assertEqual(5, Solution().maxEvents([[1,5],[1,5],[1,5],[2,3],[2,3]]))
