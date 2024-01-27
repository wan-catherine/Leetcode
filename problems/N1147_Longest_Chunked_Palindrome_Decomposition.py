import collections


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

    '''
    2024.1.27
    There is only one way for the largest possible value of k.
    '''
    def longestDecomposition_2024(self, text: str) -> int:
        length = len(text)
        l, r = 0, length - 1
        left, right = collections.deque(), collections.deque()
        res = 0
        for i in range(length):
            left.append(text[l + i])
            right.appendleft(text[r - i])
            if left == right:
                res += 1
                left, right = collections.deque(), collections.deque()
        return res
