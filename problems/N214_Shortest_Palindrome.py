"""
Use Manacher's algorithm to find the longest palindrome string centered at i.
So we can just find the maximum length palindrome string with the left end point at 0.
"""
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == s[::-1]:
            return s

        ss = "#".join("^{}$".format(s))
        l, r, length = 0, -1, len(ss)
        p = [0]*length
        index = 0
        for i in range(1, length-1):
            k = 0
            if l < r:
                k = min(p[r-i+l], r-i)
            while ss[i-k-1] == ss[i+k+1]:
                k += 1
            p[i] = k
            if i+k>r:
                r = i+k
                l = i-k
            # when i == k + 1, it means from [0:k+1] is a palindrome
            if i == k + 1:
                index = max(index, (i + p[i])//2)
        return s[index:][::-1] + s


