from unittest import TestCase
from problems.N3008_Find_Beautiful_Indices_In_The_Given_Array_II import Solution

class Test(TestCase):
    def test_beautiful_indices(self):
        self.assertListEqual([16, 33], Solution().beautifulIndices(s = "isawsquirrelnearmysquirrelhouseohmy", a = "my", b = "squirrel", k = 15))

    def test_beautiful_indices_1(self):
        self.assertListEqual([0], Solution().beautifulIndices(s = "abcd", a = "a", b = "a", k = 4))

    def test_beautiful_indices_2(self):
        self.assertListEqual([6,11,13], Solution().beautifulIndices(s = "ababababazzabababb", a = "aba", b = "bb", k = 10))
