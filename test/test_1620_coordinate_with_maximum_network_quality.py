from unittest import TestCase
from problems.N1620_Coordinate_With_Maximum_Network_Quality import Solution

class TestSolution(TestCase):
    def test_bestCoordinate(self):
        self.assertListEqual([2,1], Solution().bestCoordinate(towers = [[1,2,5],[2,1,7],[3,1,9]], radius = 2))

    def test_bestCoordinate_1(self):
        self.assertListEqual([23,11], Solution().bestCoordinate(towers = [[23,11,21]], radius = 9))

    def test_bestCoordinate_2(self):
        self.assertListEqual([1,2], Solution().bestCoordinate(towers = [[1,2,13],[2,1,7],[0,1,9]], radius = 2))

    def test_bestCoordinate_3(self):
        self.assertListEqual([0,1], Solution().bestCoordinate(towers = [[2,1,9],[0,1,9]], radius = 2))

