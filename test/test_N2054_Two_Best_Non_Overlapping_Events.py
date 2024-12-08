from unittest import TestCase
from problems.N2054_Two_Best_Non_Overlapping_Events import Solution

class TestSolution(TestCase):
    def test_max_two_events(self):
        self.assertEqual(4, Solution().maxTwoEvents([[1,3,2],[4,5,2],[2,4,3]]))

    def test_max_two_events_1(self):
        self.assertEqual(5, Solution().maxTwoEvents([[1,3,2],[4,5,2],[1,5,5]]))

    def test_max_two_events_2(self):
        self.assertEqual(8, Solution().maxTwoEvents([[1,5,3],[1,5,1],[6,6,5]]))

    def test_max_two_events_3(self):
        self.assertEqual(4, Solution().maxTwoEvents([[1,1,1],[2,2,2],[1,1,2]]))

    def test_max_two_events_4(self):
        self.assertEqual(85, Solution().maxTwoEvents([[10,83,53],[63,87,45],[97,100,32],[51,61,16]]))

    def test_max_two_events_5(self):
        self.assertEqual(165, Solution().maxTwoEvents([[66,97,90],[98,98,68],[38,49,63],[91,100,42],[92,100,22],[1,77,50],[64,72,97]]))