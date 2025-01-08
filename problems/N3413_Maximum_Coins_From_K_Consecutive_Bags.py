from typing import List

'''
Good problem!!!
Key points : 
    1. need to know it's a two pointers problem
    2. understand two o(n) :
        a. from left to right , start with the coins[i][0]
        b. from right to left , start with the coins[i][1]
    3. when compute extra, DON'T add it to cur since next loop, we will count it again
'''
class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        length = len(coins)
        def helper(coins):
            j = 0
            res = 0
            cur = 0
            for i in range(length):
                end = coins[i][0] + k - 1
                while j < length and coins[j][1] <= end:
                    cur += (coins[j][1] - coins[j][0] + 1) * coins[j][2]
                    j += 1
                extra = 0
                if j < length and coins[j][0] <= end:
                    extra += (end - coins[j][0] + 1) * coins[j][2]
                res = max(res, cur + extra)
                cur -= (coins[i][1] - coins[i][0] + 1) * coins[i][2]
            return res

        coins.sort(key=lambda x: x[0])
        arr = []
        for a, b, e in coins:
            arr.append([-b, -a, e])
        arr.sort(key=lambda x: x[0])
        return max(helper(coins), helper(arr))
