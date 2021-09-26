from unittest import TestCase
from problems.N1982_Find_Array_Given_Subset_Sums import Solution

class TestSolution(TestCase):
    def test_recover_array(self):
        self.assertListEqual([1,2,-3], Solution().recoverArray(n = 3, sums = [-3,-2,-1,0,0,1,2,3]))

    def test_recover_array_1(self):
        self.assertListEqual([0,0], Solution().recoverArray(n = 2, sums = [0,0,0,0]))

    def test_recover_array_2(self):
        self.assertListEqual([0,-1,4,5], Solution().recoverArray(n = 4, sums = [0,0,5,5,4,-1,4,9,9,-1,4,3,4,8,3,8]))

    def test_recover_array_3(self):
        self.assertListEqual([-45,-80,-182,276,296,-509,-653,721], Solution().recoverArray(8,
[408,-307,86,-886,-164,784,-377,49,-1424,14,0,310,-589,162,735,872,-80,557,-590,-290,319,-51,-1173,-715,216,-1207,-392,333,-437,539,276,459,522,-233,527,390,-472,-388,-521,-486,-1011,-457,-278,596,-452,-62,-145,-262,-1048,-427,-852,-159,-402,171,264,704,-1287,-210,-126,345,114,1168,443,-263,-119,-1389,-502,-347,-338,117,57,-880,494,378,-897,-733,1066,212,1293,-623,137,488,492,37,-165,508,-1128,-946,201,265,-639,167,364,23,-960,710,770,-293,261,30,-635,-482,-509,-911,-15,34,284,-772,-327,-698,997,-45,-441,-57,-206,196,-343,952,-915,151,231,458,-114,515,82,383,1248,428,344,-668,-604,-227,363,595,239,-817,721,-308,-736,-161,986,306,-395,-691,-619,972,-270,51,-95,-415,-664,-199,251,296,-11,-539,-653,414,-835,892,-50,-460,-816,659,-966,102,815,602,-190,326,-372,-81,94,87,69,131,-125,-258,-703,-12,-634,1017,560,-771,755,-1242,-1068,-245,-866,1213,-176,219,-931,-182,246,-31,18,1031,68,-213,299,-1162,1111,572,63,-1469,-357,690,182,-358,-239,-1148,226,447,-559,-225,-540,-1113,-554,-584,-1344,281,477,-313,917,-422,132,-778,790,-475,-244,-1093,-684,-991,835,463,-670,-495,413,641,937,-17,-131,739,676,181,-520,640,-440,-96,6,-194,-1193,-407,-566,-748]))