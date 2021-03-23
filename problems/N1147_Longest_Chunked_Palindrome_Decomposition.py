class Solution:
    def longestDecomposition(self, text: str) -> int:
        def helper(s, cur):
            length = len(s)
            if s == "":
                return cur
            if s == s[::-1]:
                return length + cur

            ans = 0
            for i in range(1, length + 1):
                if s[:i] == s[-i:]:
                    if i == length:
                        ans = max(ans, helper(s[i:-i], cur + 1))
                    else:
                        ans = max(ans, helper(s[i:-i], cur + 2))
            return ans

        return helper(text, 0)