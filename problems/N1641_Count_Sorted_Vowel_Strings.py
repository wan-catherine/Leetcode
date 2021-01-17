class Solution(object):
    def countVowelStrings_before(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = {"a":1, "e":1, "i":1, "o":1, "u":1}
        if n == 1:
            return 5

        for i in range(2, n+1):
            num = sum(d.values())
            val = 0
            for c in ["a","e","i","o","u"]:
                t = d[c]
                d[c] = num - val
                val += t
        return sum(d.values())

    """
    dp[i][k] : number of the strings which ith char is k . 
    """
    def countVowelStrings(self, n):
        dp = [[0] * 5 for _ in range(n)]
        for k in range(5):
            dp[0][k] = 1

        for i in range(1, n):
            for k in range(5):
                for j in range(k+1):
                    dp[i][k] += dp[i-1][j]
        return sum(dp[-1])

