import collections

class Solution(object):
    def numberOfArrays(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        length = len(s)
        dp = [0] * (length + 1)
        dp[0] = 1
        last_numbers = collections.defaultdict(int)
        for i, c in enumerate(s):
            num = int(s[i])
            new_last = collections.defaultdict(int)
            if num and num <= k:
                dp[i+1] = dp[i]
                new_last[num] += dp[i]
            for ln in last_numbers:
                nln = ln*10 + num
                if nln <= k:
                    dp[i+1] += last_numbers[ln]
                    new_last[nln] += last_numbers[ln]
            dp[i+1] %= (10**9 + 7)
            last_numbers = new_last
        return dp[-1] % (10**9 + 7)


