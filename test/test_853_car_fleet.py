from unittest import TestCase
from problems.N853_Car_Fleet import Solution

class TestSolution(TestCase):
    def test_carFleet(self):
        self.assertEqual(3, Solution().carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))

    def test_carFleet_1(self):
        self.assertEqual(1, Solution().carFleet(target = 10, position = [3], speed = [3]))

    def test_carFleet_2(self):
        self.assertEqual(2, Solution().carFleet(10, [6,8], [3,2]))

    def test_carFleet_3(self):
        self.assertEqual(1, Solution().carFleet(10, [0,4,2], [2,1,3]))

