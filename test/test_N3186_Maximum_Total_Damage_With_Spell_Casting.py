from unittest import TestCase
from problems.N3186_Maximum_Total_Damage_With_Spell_Casting import Solution

class TestSolution(TestCase):
    def test_maximum_total_damage(self):
        self.assertEquals(6, Solution().maximumTotalDamage([1,1,3,4]))

    def test_maximum_total_damage_1(self):
        self.assertEquals(13, Solution().maximumTotalDamage([7,1,6,6]))

    def test_maximum_total_damage_2(self):
        self.assertEquals(12, Solution().maximumTotalDamage([3,3,1,2,3,3,1,2,1]))
