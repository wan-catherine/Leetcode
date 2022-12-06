class Solution:
    def countPalindromes(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        s = '#' + s + '#'
        length = len(s)
        dpf, dfa = [[[0] * length for _ in range(10)] for _ in range(10)], [[[0] * length for _ in range(10)] for _ in range(10)]

        cur = [0] * 10
        for k in range(1, length - 1):
            if k > 1:
                cur[int(s[k-1])] += 1
            for i in range(10):
                for j in range(10):
                    dpf[i][j][k] = dpf[i][j][k-1]
                    if s[k] == str(j):
                        dpf[i][j][k] += cur[i]

        cur = [0] * 10
        for k in range(length-2, 0, -1):
            if k < length - 2:
                cur[int(s[k+1])] += 1
            for i in range(10):
                for j in range(10):
                    dfa[i][j][k] = dfa[i][j][k+1]
                    if s[k] == str(j):
                        dfa[i][j][k] += cur[i]

        res = 0
        for i in range(10):
            for j in range(10):
                for k in range(3, length-3):
                    res += dpf[i][j][k-1] * dfa[i][j][k+1]
                    res %= MOD
        return res % MOD