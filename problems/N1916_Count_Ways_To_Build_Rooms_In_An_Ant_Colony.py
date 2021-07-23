import collections
from typing import List


class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        m = 10**9+7
        length = len(prevRoom)
        dp, count = [0] * length, [0] * length
        next = collections.defaultdict(list)
        for i in range(1, length):
            next[prevRoom[i]].append(i)
        f = [1] * (length + 1)
        for i in range(1, length + 1):
            f[i] = f[i-1] * i % m

        def inv(x):
            s = 1
            while x > 1:
                s = s * (m - m // x) % m
                x = m % x
            return s

        def dfs(node):
            if not next[node]:
                dp[node] = 1
                count[node] = 1
                return
            total = 0
            for n in next[node]:
                dfs(n)
                total += count[n]
            res = f[total]
            for n in next[node]:
                res = res * inv(f[count[n]]) % m
                res = res * dp[n] % m
            count[node] = total + 1
            dp[node] = res
        dfs(0)
        return dp[0] % m