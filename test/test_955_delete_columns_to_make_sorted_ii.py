from unittest import TestCase
from problems.N955_Delete_Columns_To_Make_Sorted_II import Solution

class TestSolution(TestCase):
    def test_minDeletionSize(self):
        self.assertEqual(1, Solution().minDeletionSize(["ca","bb","ac"]))

    def test_minDeletionSize_1(self):
        self.assertEqual(1, Solution().minDeletionSize(["xga","xfb","yfa"]))

    def test_minDeletionSize_2(self):
        self.assertEqual(0, Solution().minDeletionSize(["xc","yb","za"]))

    def test_minDeletionSize_3(self):
        self.assertEqual(3, Solution().minDeletionSize(["zyx","wvu","tsr"]))

    def test_minDeletionSize_4(self):
        self.assertEqual(1, Solution().minDeletionSize(["abx","agz","bgc","bfc"]))

    def test_minDeletionSize_5(self):
        self.assertEqual(4, Solution().minDeletionSize(["bwwdyeyfhc","bchpphbtkh","hmpudwfkpw","lqeoyqkqwe","riobghmpaa","stbheblgao","snlaewujlc","tqlzolljas","twdkexzvfx","wacnnhjdis"]))

    def test_minDeletionSize_6(self):
        self.assertEqual(6, Solution().minDeletionSize(["hdbbaomiyk","amcdtrnhjn","fheqnqdkjq","mfeluiclbm","jkexmcstwn","egfmxwjxdj","ayhowbifcx","swhykufgfk","vxhdwxuhwj","johfdcfojv","rnircklfcm","lzkwfqomcz","fvkkhzomgb","aukuoedptv","eimzwmlgxj","ptmnmgppso","oknfgdtweb","mtnukewwir","nlowbhwjdm","tcovbbvuuw","ilqyvtgnfv","nrqgupdyyg","wnrdwmsnzt","rosqrtdeus","bysheeghqg","ciswvgqqlf","uwteztkmqf","tbumqubzdb","dqxbfiwuvm","atxbvdiywo"]))