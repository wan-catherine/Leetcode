class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        length = len(s)
        s = list(s)
        res, count = 0, 0
        for i in range(length//2):
            j = length - 1 - count
            while s[j] != s[i]:
                j -= 1
            if i == j:
                res += length // 2 - i
                continue
            k = length - 1 - count - j
            res += k
            while k > 0:
                s[j], s[j+1] = s[j+1], s[j]
                k -= 1
                j += 1
            count += 1
        return res
