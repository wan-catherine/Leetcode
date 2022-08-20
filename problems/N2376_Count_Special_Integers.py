import math
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        sn = str(n)
        length = len(sn)
        res = 0
        for i in range(1, length):
            res += math.perm(10, i) - math.perm(9, i-1)
        visited = [0] * 10
        def dfs(idx):
            nonlocal res
            if idx >= length:
                res += 1
                return
            for i in range(10):
                if i == 0 and idx == 0:
                    continue
                if visited[i]:
                    continue
                if i < int(sn[idx]):
                    res += math.perm(10-(idx+1), length - idx - 1)
                elif i == int(sn[idx]):
                    visited[i] = 1
                    dfs(idx+1)
                    visited[i] = 0
        dfs(0)
        return res