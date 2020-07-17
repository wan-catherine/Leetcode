"""
Key point :
    calculate the accumulate frequency of all characters for all prefixes of the string
"""
class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        counters = [[0]*26]

        for i in range(len(s)):
            temp = counters[-1][:]
            temp[ord(s[i]) - ord('a')] += 1
            counters.append(temp)

        res = []
        for left, right, k in queries:
            val = 0
            for i in range(26):
                if (counters[right+1][i] - counters[left][i]) % 2:
                    val += 1

            if val > 2*k + 1:
                res.append(False)
            else:
                res.append(True)
        return res

