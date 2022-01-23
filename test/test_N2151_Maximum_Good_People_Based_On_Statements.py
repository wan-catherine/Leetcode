from unittest import TestCase
from problems.N2151_Maximum_Good_People_Based_On_Statements import Solution

class TestSolution(TestCase):
    def test_maximum_good(self):
        self.assertEqual(2, Solution().maximumGood([[2,1,2],[1,2,2],[2,0,2]]))

    def test_maximum_good_1(self):
        self.assertEqual(1, Solution().maximumGood([[2,0],[0,2]]))

    def test_maximum_good_2(self):
        self.assertEqual(0, Solution().maximumGood([[2,0,0,2,2,0,1,2],[0,2,1,0,0,1,1,0],[0,0,2,0,2,0,1,2],[1,0,2,2,1,0,0,1],[1,1,2,1,2,2,1,0],[2,0,0,0,1,2,0,0],[0,2,2,0,2,1,2,0],[2,1,2,0,0,1,0,2]]))

    def test_maximum_good_3(self):
        self.assertEqual(3, Solution().maximumGood([[2,2,2,2,2,2],[2,2,2,1,1,2],[2,2,2,2,2,2],[0,1,0,2,1,2],[0,1,2,1,2,0],[0,0,1,0,2,2]]))

    def test_maximum_good_4(self):
        self.assertEqual(1, Solution().maximumGood([[2,1,0,0,2],[2,2,1,0,2],[0,2,2,1,0],[2,0,0,2,0],[2,0,0,1,2]]))