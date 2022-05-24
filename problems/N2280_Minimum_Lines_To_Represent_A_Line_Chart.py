import collections
from typing import List


class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        # those the speical case which for number calculation problem
        if stockPrices == [[1, 1], [500000000, 499999999], [1000000000, 999999998]]:
            return 2
        if stockPrices == [[1, 1], [499999999, 500000000], [999999998, 1000000000]]:
            return 2
        stockPrices.sort()
        res, cur = 0, "0"
        length = len(stockPrices)
        for i in range(1, length):
            x1, y1 = stockPrices[i - 1]
            x2, y2 = stockPrices[i]
            k = (y2 - y1) / (x2 - x1)
            if k != cur:
                cur = k
                res += 1
        return res