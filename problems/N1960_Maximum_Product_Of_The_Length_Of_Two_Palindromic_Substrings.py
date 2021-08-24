class Solution:
    def maxProduct(self, s: str) -> int:
        # manacher's algo
        length = len(s)
        s = '^' + s + '&'
        p = [0] * length
        l, r = 0, -1
        for i in range(1, length+1):
            k = 0
            if i < r:
                j = r - i + l
                k = min(p[j-1], r - i)
            while s[i-k-1] == s[i+k+1]:
                k += 1
            p[i-1] = k
            if i + k > r:
                r = i + k
                l = i - k

        # left[i] : left of index i (include i), the longest palindrome length .
        # right[i] : right of index i (include i), the longest palindrome length .

        left = [0] * length
        left[0] = 1
        j = 0
        for i in range(1, length):
            # j linear increase
            while j < i and p[j] + j < i:
                j += 1
            left[i] = max(left[i-1], (i-j) * 2 + 1)
        right = [0] * length
        right[-1] = 1
        j = length - 1
        for i in range(length-2, -1, -1):
            while j > i and j - p[j] > i:
                j -= 1
            right[i] = max(right[i+1], (j-i) * 2 + 1)
        res = 0
        for i in range(length - 1):
            res = max(res, left[i] * right[i+1])
        return res