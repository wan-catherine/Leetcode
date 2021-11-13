"""
Palindrome check:
    1. single character : a, b, c....
    2. two same characters : aa, bb, cc, ...
    3, if length > 2 and s[first] = s[last], then it depends on the substring between first and last character.
        first, second, ..., last_second, last  will be same as second,...,last_second
"""

class Solution(object):
    def countSubstrings_n_n(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        dp = [[0] * length for _ in range(length)]
        res = 0
        for i in range(length):
            for start in range(length):
                end = start + i
                if end >= length:
                    break
                if i == 0:
                    dp[start][end] = 1
                elif s[start] == s[end]:
                    if i == 1 :
                        dp[start][end] = 1
                    elif start + 1 <= end - 1:
                        dp[start][end] = dp[start+1][end-1]
                res += dp[start][end]
        return res

    """
    1. only one character, then extend to left and right : a -> bab -> cbabc
    2. two characters, then extend to left and right : aa -> baab -> cbaabc
    """
    def countSubstrings_two_pass(self, s):
        if not s:
            return 0

        count = self.helper(s, 1)
        count += self.helper(s, 2)
        return count

    def helper(self, s, l ):
        count = 0
        length = len(s)
        for i in range(l-1, length):
            if s[i] != s[i-l+1]:
                continue
            count += 1
            start, end = i - l, i + 1

            while start >= 0 and end < length:
                if s[start] == s[end]:
                    count += 1
                    start -= 1
                    end += 1
                else:
                    break
        return count

    """
    Manacher's Algorithm
    
    Notice how to get the number of palindromic substrings
    """
    def countSubstrings(self, s):
        s_new = '#'.join("^{}*".format(s))
        l, r, length = 0, -1, len(s_new)
        p = [0] * length

        for i in range(1, length-1):
            if i < r:
                j = r - i + l
                p[i] = min(p[j], r - i)

            while s_new[i - p[i] - 1] == s_new[i + p[i] + 1]:
                p[i] += 1

            if i + p[i] > r:
                l = i - p[i]
                r = i + p[i]
        return sum([(i+1)//2 for i in p])

    # update at 20211113
    def countSubstrings(self, s: str) -> int:
        ns = '#'.join("^{0}$".format(s))
        length = len(ns)
        l, r = 0, -1
        p = [0] * length
        for i in range(1, length - 1):
            k = 0
            if i < r:
                j = l + r - i
                k = min(p[j], r - i)
            while ns[i - k - 1] == ns[i + k + 1]:
                k += 1
            p[i] = k
            if i + k > r:
                l = i - k
                r = i + k
        ans = 0
        # print(p)
        for i in range(1, length - 1):
            n = p[i]
            if ns[i] == '#':
                ans += n // 2
            else:
                ans += n // 2 + 1
        return ans