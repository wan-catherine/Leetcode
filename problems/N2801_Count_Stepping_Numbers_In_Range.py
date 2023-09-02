class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        MOD = 10 ** 9 + 7
        mapping = {}
        def dfs(l, prev, isSame, sn):
            if l == 0:
                return 1
            if (l, prev, isSame, sn) in mapping:
                return mapping[(l, prev, isSame, sn)]
            res = 0
            length = len(sn)
            if not isSame:
                if prev + 1 <= 9:
                    res = (res + dfs(l - 1, prev + 1, False, sn)) % MOD
                if prev - 1 >= 0:
                    res = (res + dfs(l - 1, prev - 1, False, sn)) % MOD
            else:
                d = int(sn[length - l])
                if prev + 1 < d:
                    res = (res + dfs(l - 1, prev + 1, False, sn)) % MOD
                elif prev + 1 == d:
                    res = (res + dfs(l - 1, prev + 1, True, sn)) % MOD
                if 0 <= prev - 1 < d:
                    res = (res + dfs(l - 1, prev - 1, False, sn)) % MOD
                elif prev - 1 >= 0 and prev - 1 == d:
                    res = (res + dfs(l - 1, prev - 1, True, sn)) % MOD
            mapping[(l, prev, isSame, sn)] = res % MOD
            return res % MOD
        def helper(num):
            length = len(num)
            res = 0
            for i in range(1, length):
                for j in range(1, 10):
                    res = (res + dfs(i - 1, j, False, num)) % MOD
            d = int(num[0])
            for i in range(1, d):
                res = (res + dfs(length - 1, i, False, num)) % MOD
            res = (res + dfs(length - 1, d, True, num)) % MOD
            return res

        def check(num):
            length = len(num)
            for i in range(1, length):
                if abs(int(num[i]) - int(num[i-1])) != 1:
                    return 0
            return 1

        return (helper(high) - helper(low) + check(low)) % MOD



