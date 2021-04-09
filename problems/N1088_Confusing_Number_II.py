class Solution:
    def confusingNumberII(self, N: int) -> int:
        sn = str(N)
        length = len(sn)
        pairs = [('1', '1'), ('0', '0'), ('8', '8'), ('6', '9'), ('9', '6')]
        ans = 0
        def helper(n):
            nonlocal ans
            if n == 0:
                return ['']
            if n == 1:
                cur = ['1', '0', '8']
            else:
                cur = []
                prev = helper(n - 2)
                for p in prev:
                    for pair in pairs:
                        s = pair[0] + p + pair[1]
                        cur.append(s)
            for c in cur:
                if (c[0] != '0' or c == '0') and int(c) <= N:
                    ans += 1
            return cur

        helper(length)
        helper(length - 1)

        dp = [0] * (length + 1)
        dp[1] = 5
        for i in range(2, length):
            dp[i] = 4 * 5 ** (i - 1)
        total = sum(dp[:-1])
        for p in range(length):
            i = int(sn[p])
            if i >= 9:
                f = 4
            elif i >= 8:
                f = 3
            elif i >= 6:
                f = 3 - (1 if i == 6 else 0)
            elif i >= 1:
                f = 2 - (1 if i == 1 else 0)
            elif i == 0:
                f = 0
            if p == 0:
                f -= 1
            total += (f * 5 ** (length - p - 1))
            if i not in [0,1,6,8,9]:
                break
            if p == length -1 and i in [0,1,6,8,9]:
                total += 1
        return total - ans









