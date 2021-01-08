from unittest import TestCase
from problems.N757_Set_Intersection_Size_At_Least_Two import Solution

class TestSolution(TestCase):
    def test_intersectionSizeTwo(self):
        self.assertEqual(3, Solution().intersectionSizeTwo([[1,3],[1,4],[2,5],[3,5]]))

    def test_intersectionSizeTwo_1(self):
        self.assertEqual(5, Solution().intersectionSizeTwo([[1,2],[2,3],[2,4],[4,5]]))

    def test_intersectionSizeTwo_2(self):
        self.assertEqual(5, Solution().intersectionSizeTwo([[1,3],[3,7],[5,7],[7,8]]))

    def test_intersectionSizeTwo_3(self):
        self.assertEqual(6, Solution().intersectionSizeTwo([[4,7],[5,8],[7,9],[2,6],[0,1],[1,4],[1,9],[0,5],[5,10],[7,8]]))

    def test_intersectionSizeTwo_4(self):
        self.assertEqual(5, Solution().intersectionSizeTwo([[0,3],[0,4],[0,9],[8,9],[0,7],[1,4],[6,10],[0,4],[3,7],[6,8]]))
