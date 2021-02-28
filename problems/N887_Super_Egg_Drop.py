from math import inf


class Solution:
    # d[i][j]: means there are i eggs and j floors, we can drop at least d[i][j] to find the Fth floor
    # i <= j : there are j floors, so we need j eggs at most .
    # for each number of eggs, we can try it from the first to the last floor, then use the least one
    # at each floor, there are two situations:
    #   1.broken : d[i-1][j-1]   used one egg, so minus 1 from i, then we need go down floors
    #   2.not broken: d[i][k-j] still have i eggs, need to go up floors

    def superEggDrop_timeout(self, K: int, N: int) -> int:
        if K > N:
            K = N
        dp_table = [[None for i in range(N+1)] for j in range(K+1)]
        for j in range(N+1):
            dp_table[0][j] = 0
            dp_table[1][j] = j
        for i in range(K+1):
            dp_table[i][0] = 0
        for i in range(2, K+1):
            for j in range(1, N+1):
                if i > j:
                    dp_table[i][j] = dp_table[i-1][j]
                    continue
                res = float(inf)
                # for k in range(1, j+1):
                #     res = min(res, max(dp_table[i][j-k]+1,dp_table[i-1][k-1]+1))
                lo,hi = 1, j
                while lo <= hi:
                    mid = (lo + hi) // 2
                    broken = dp_table[i-1][mid-1]
                    not_broken = dp_table[i][j-mid]
                    if broken > not_broken:
                        hi = mid - 1
                        res = min(res, broken + 1)
                    else:
                        lo = mid + 1
                        res = min(res, not_broken + 1)

                dp_table[i][j] = res
        return dp_table[-1][-1]

    # d[i][j] = m : use i eggs, for m floors, we can drop at least j times
    def superEggDrop_(self, K: int, N: int) -> int:
        if K > N:
            K = N
        dp_table = [[0 for i in range(N+1)] for j in range(K+1)]
        m = 0
        while dp_table[K][m] < N:
            m += 1
            for i in range(1, K+1):
                dp_table[i][m] = dp_table[i][m-1] + dp_table[i-1][m-1] + 1

        return m

    # don't understand this solution.
    # why? why? why?
    # ?????????? help
    def superEggDrop_fast(self, K: int, N: int) -> int:
        drops = 0
        floors = [0 for _ in range(K + 1)]
        while floors[K] < N:
            for eggs in range(K, 0, -1):
                floors[eggs] += 1 + floors[eggs - 1]
            drops += 1
        return drops

    """
    Update at 2021027
    dp[i][j] : the highest level of a building we can know when we have i eggs and j chance to throw eggs . 
    
    """
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0] * (N+1) for _ in range(K+1)]
        for m in range(1, N+1):
            for k in range(1, K+1):
                dp[k][m] = dp[k][m-1] + dp[k-1][m-1] + 1
                if dp[k][m] >= N:
                    return m
        return N
