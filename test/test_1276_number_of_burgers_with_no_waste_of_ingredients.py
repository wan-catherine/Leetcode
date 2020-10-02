from unittest import TestCase
from problems.N1276_Number_Of_Burgers_With_No_Waste_Of_Ingredients import Solution

class TestSolution(TestCase):
    def test_numOfBurgers(self):
        self.assertListEqual([1,6], Solution().numOfBurgers(16, 7))

    def test_numOfBurgers_1(self):
        self.assertListEqual([], Solution().numOfBurgers(17, 4))

    def test_numOfBurgers_2(self):
        self.assertListEqual([], Solution().numOfBurgers(4, 17))

    def test_numOfBurgers_3(self):
        self.assertListEqual([0,0], Solution().numOfBurgers(0, 0))

    def test_numOfBurgers_4(self):
        self.assertListEqual([0,1], Solution().numOfBurgers(2, 1))

    def test_numOfBurgers_5(self):
        self.assertListEqual([], Solution().numOfBurgers(2385088, 164763))

