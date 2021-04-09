class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        if N <= 10:
            return 0
        st = str(N)
        length = len(st)
        dp = [0] * (length + 1)
        dp[1] = 10
        dp[2] = 81
        for i in range(3, length):
            dp[i] = 81
            for j in range(2, i):
                dp[i] *= (9 - j + 1)
        ans = sum(dp[:-1])

        unused = [1] * 10
        arr = [int(i) for i in st]
        for p in range(length):
            i = arr[p]
            val = i - (1 if p == 0 else 0)
            if p == length - 1:   # the last digit, should be one of situation.
                val += 1
            for k in range(val):
                if unused[k] == 0:
                    val -= 1
            val = max(val, 0)
            for j in range(length - p - 1):
                val *= sum(unused) - 1 - j
            ans += val
            if unused[i] == 0:  # if it shows before, no matter what for the later , it will be always duplicated. 
                break
            unused[i] = 0
        return N - ans + 1
