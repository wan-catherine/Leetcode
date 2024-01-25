from typing import List


class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        tokens.sort()
        length = len(tokens)
        total = sum(tokens)
        return self.helper(0, length-1, P, total, 0, tokens)

    def helper(self, i, j, p, total, ans, tokens):
        if i > j:
            return ans
        if p >= total:
            return ans + j - i + 1
        if p < tokens[i] and ans == 0:
            return ans
        if p >= tokens[i]:
            return self.helper(i+1, j, p-tokens[i], total-tokens[i], ans+1, tokens)

        return self.helper(i+1, j-1, p+tokens[j]-tokens[i], total-tokens[j]-tokens[i], ans, tokens)

    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        length = len(tokens)

        res, ans = 0, 0
        l, r = 0, length - 1
        cur = power
        while l <= r:
            if tokens[l] > cur:
                break
            t = 0
            idx = l
            while idx <= r and t + tokens[idx] <= cur:
                t += tokens[idx]
                idx += 1
            res = max(res, ans + idx - l)

            cur -= tokens[l]
            l += 1
            cur += tokens[r]
            r -= 1

        return res
