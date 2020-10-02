from unittest import TestCase
from problems.N1282_Group_The_People_Given_The_Group_SIze_They_Belong_To import Solution

class TestSolution(TestCase):
    def test_groupThePeople(self):
        self.assertListEqual([[5],[0,1,2],[3,4,6]], Solution().groupThePeople([3,3,3,3,3,1,3]))

    def test_groupThePeople_1(self):
        self.assertListEqual([[1],[0,5],[2,3,4]], Solution().groupThePeople([2,1,3,3,3,2]))
