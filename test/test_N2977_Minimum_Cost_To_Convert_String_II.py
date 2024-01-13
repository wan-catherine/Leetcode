from unittest import TestCase
from problems.N2977_Minimum_Cost_To_Convert_String_II import Solution

class TestSolution(TestCase):
    def test_minimum_cost(self):
        self.assertEqual(28, Solution().minimumCost(source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]))

    def test_minimum_cost_1(self):
        self.assertEqual(9, Solution().minimumCost(source = "abcdefgh", target = "acdeeghh", original = ["bcd","fgh","thh"], changed = ["cde","thh","ghh"], cost = [1,3,5]))

    def test_minimum_cost_2(self):
        self.assertEqual(-1, Solution().minimumCost(source = "abcdefgh", target = "addddddd", original = ["bcd","defgh"], changed = ["ddd","ddddd"], cost = [100,1578]))
