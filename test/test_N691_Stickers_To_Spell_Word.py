from unittest import TestCase
from problems.N691_Stickers_To_Spell_Word import Solution

class TestSolution(TestCase):
    def test_min_stickers(self):
        self.assertEqual(3, Solution().minStickers(["with", "example", "science"], "thehat"))

    def test_min_stickers_1(self):
        self.assertEqual(-1, Solution().minStickers(["notice", "possible"], "basicbasic"))

    def test_min_stickers_2(self):
        self.assertEqual(3, Solution().minStickers(["these","guess","about","garden","him"], "atomher"))