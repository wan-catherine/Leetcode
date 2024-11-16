from unittest import TestCase
from problems.N3307_Find_The_Kth_Character_In_String_Game_II import Solution

class TestSolution(TestCase):
    def test_kth_character(self):
        self.assertEqual('a', Solution().kthCharacter(k = 5, operations = [0,0,0]))

    def test_kth_character_1(self):
        self.assertEqual('b', Solution().kthCharacter(k = 10, operations = [0,1,0,1]))

    def test_kth_character_2(self):
        self.assertEqual('a', Solution().kthCharacter(k = 3, operations = [1,0]))
