"""
State compression DP
"""
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10 ** 9 + 7
        status = []
        for sta in range(3 ** m):
            cur = sta
            li = []
            flag = True
            for i in range(m):
                d = cur % 3
                if li and li[-1] == d:
                    flag = False
                    break
                cur //= 3
                li.append(d)
            if flag:
                status.append(sta)
        def check(i, j):
            nonlocal m
            ii, jj = status[i], status[j]
            for idx in range(m):
                if ii % 3 == jj % 3:
                    return False
                ii //= 3
                jj //= 3
            return True

        length = len(status)
        dp = [1] * length
        dp_new = [0] * length
        for i in range(1, n):
            for j in range(length):
                dp_new[j] = 0
                for k in range(length):
                    if check(j, k):
                        dp_new[j] = (dp_new[j] + dp[k]) % mod
            # here must deep copy the whole dp_new
            dp = dp_new[:]
        return sum(dp) % mod
