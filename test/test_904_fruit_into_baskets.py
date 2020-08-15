from unittest import TestCase
from problems.N904_Fruit_Into_Baskets import Solution

class TestSolution(TestCase):
    def test_totalFruit(self):
        self.assertEqual(3, Solution().totalFruit([1,2,1]))

    def test_totalFruit_1(self):
        self.assertEqual(3, Solution().totalFruit([0,1,2,2]))

    def test_totalFruit_2(self):
        self.assertEqual(4, Solution().totalFruit([1,2,3,2,2]))

    def test_totalFruit_3(self):
        self.assertEqual(5, Solution().totalFruit([3,3,3,1,2,1,1,2,3,3,4]))

    def test_totalFruit_4(self):
        self.assertEqual(3, Solution().totalFruit([1,0,3,4,3]))
