from unittest import TestCase
from problems.N2070_Most_Beautiful_Item_For_Each_Query import Solution

class TestSolution(TestCase):
    def test_maximum_beauty(self):
        self.assertListEqual([2,4,5,5,6,6], Solution().maximumBeauty(items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]))

    def test_maximum_beauty_1(self):
        self.assertListEqual([4], Solution().maximumBeauty(items = [[1,2],[1,2],[1,3],[1,4]], queries = [1]))

    def test_maximum_beauty_2(self):
        self.assertListEqual([0], Solution().maximumBeauty(items = [[10,1000]], queries = [5]))

    def test_maximum_beauty_3(self):
        self.assertListEqual([962,962,962,962,746,962,962,962,946,962,962,919,746,746,962,962,962,919,962], Solution().maximumBeauty([[193,732],[781,962],[864,954],[749,627],[136,746],[478,548],[640,908],[210,799],[567,715],[914,388],[487,853],[533,554],[247,919],[958,150],[193,523],[176,656],[395,469],[763,821],[542,946],[701,676]]
,[885,1445,1580,1309,205,1788,1214,1404,572,1170,989,265,153,151,1479,1180,875,276,1584]))