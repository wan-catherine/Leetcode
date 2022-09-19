from typing import List


class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        pos, neg = [], []
        for u, v in transactions:
            if u - v > 0:
                neg.append([u, v])
            else:
                pos.append([u, v])
        neg.sort(key=lambda x : x[1])
        pos.sort(key=lambda x : -x[0])
        res = 0
        cur = 0
        arr = neg + pos
        length = len(arr)
        for i in range(length):
            res = max(cur + arr[i][0], res)
            cur += arr[i][0] - arr[i][1]

        return res