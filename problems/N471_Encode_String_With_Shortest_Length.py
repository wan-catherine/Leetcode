"""
Given a non-empty string, encode the string such that its encoded length is the shortest.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.

Note:

k will be a positive integer.
If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return any of them.

Example 1:

Input: s = "aaa"
Output: "aaa"
Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.
Example 2:

Input: s = "aaaaa"
Output: "5[a]"
Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
Example 3:

Input: s = "aaaaaaaaaa"
Output: "10[a]"
Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5, which is the same as "10[a]".
Example 4:

Input: s = "aabcaabcd"
Output: "2[aabc]d"
Explanation: "aabc" occurs twice, so one answer can be "2[aabc]d".
Example 5:

Input: s = "abbbabbbcabbbabbbc"
Output: "2[2[abbb]c]"
Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to "2[abbb]c", so one answer can be "2[2[abbb]c]".

Constraints:

1 <= s.length <= 150
s consists of only lowercase English letters.
"""
class Solution:
    def encode(self, s: str) -> str:
        def helper(a, e):
            st = s[a:e+1]
            res = st
            for l in range(1, e-a+1):
                if (e-a+1)%l:
                    continue
                count = (e-a+1) // l
                if st != st[:l] * count:
                    continue
                t = f"{count}[{dp[a][a+l-1]}]"
                if len(t) < len(res):
                    res = t
            return res

        length = len(s)
        dp = [[None] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = s[i]

        for l in range(2, length+1):
            for i in range(length-l+1):
                j = i + l - 1
                dp[i][j] = helper(i, j)
                for k in range(i, j):
                    if len(dp[i][j]) > len(dp[i][k]) + len(dp[k+1][j]):
                        dp[i][j] = dp[i][k] + dp[k+1][j]
        return dp[0][-1]