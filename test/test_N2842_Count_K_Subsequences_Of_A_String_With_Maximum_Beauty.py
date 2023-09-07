from unittest import TestCase
from problems.N2842_Count_K_Subsequences_Of_A_String_With_Maximum_Beauty import Solution

class TestSolution(TestCase):
    def test_count_ksubsequences_with_max_beauty(self):
        self.assertEquals(4, Solution().countKSubsequencesWithMaxBeauty(s = "bcca", k = 2))

    def test_count_ksubsequences_with_max_beauty_1(self):
        self.assertEquals(2, Solution().countKSubsequencesWithMaxBeauty(s = "abbcd", k = 4))

    def test_count_ksubsequences_with_max_beauty_2(self):
        self.assertEquals(0, Solution().countKSubsequencesWithMaxBeauty(s = "dd", k = 2))

    def test_count_ksubsequences_with_max_beauty_3(self):
        self.assertEquals(8, Solution().countKSubsequencesWithMaxBeauty(s = "sdsidx", k = 3))

    def test_count_ksubsequences_with_max_beauty_4(self):
        self.assertEquals(12, Solution().countKSubsequencesWithMaxBeauty(s = "jyuhiyzjuk", k = 2))

