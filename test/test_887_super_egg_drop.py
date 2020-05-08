from unittest import TestCase
from problems.N887_Super_Egg_Drop import Solution

class TestSolution(TestCase):
    def test_superEggDrop(self):
        self.assertEqual(2, Solution().superEggDrop(1,2))

    def test_superEggDrop_1(self):
        self.assertEqual(3, Solution().superEggDrop(2, 6))

    def test_superEggDrop_2(self):
        self.assertEqual(4, Solution().superEggDrop(3, 14))

