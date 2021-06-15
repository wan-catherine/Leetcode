from unittest import TestCase
from problems.N1884_Egg_Drop_With_2_Eggs_And_N_Floors import Solution

class TestSolution(TestCase):
    def test_two_egg_drop(self):
        self.assertEqual(2, Solution().twoEggDrop(2))

    def test_two_egg_drop_1(self):
        self.assertEqual(14, Solution().twoEggDrop(100))
