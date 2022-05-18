import collections
import string

"""
The key point here is how to make sure there is 1 and -1 in the substring. 

1 <= s.length <= 10**4 
Gives a hint that there should be O(kn), k can be 26 or 26 ** 2. 

"""
class Solution:
    def largestVariance(self, s: str) -> int:
        length = len(s)
        ct = collections.Counter(s)

        def helper(num):
            l = len(num)
            dp = [0] * l
            dp[0] = num[0]
            for i in range(1, l):
                dp[i] = max(num[i], dp[i - 1] + num[i])
            current = 0
            res = 0
            for i in range(l - 1, -1, -1):
                current = max(num[i], num[i] + current)
                if num[i] == -1:
                    res = max(res, dp[i] + current - num[i])
            return res

        res = 0
        for i in string.ascii_lowercase:
            for j in string.ascii_lowercase:
                if i == j or i not in ct or j not in ct:
                    continue
                num = []
                for c in range(length):
                    if s[c] == i:
                        num.append(1)
                    elif s[c] == j:
                        num.append(-1)
                res = max(res, helper(num))
        return res