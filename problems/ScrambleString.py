class Solution:
    def isScramble_(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == None and s2 == None:
            return True

        if sorted(s1) != sorted(s2):
            return False

        return self.helper(s1, s2)

    def helper(self, s1, s2):
        print(s1, s2)

        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        res = False

        for i in range(1,len(s1)):
            if (self.helper(s1[:i], s2[:i]) and self.helper(s1[i:], s2[i:]) or
                self.helper(s1[:i], s2[-i:]) and self.helper(s1[i:], s2[:-i])):
                res = True
                break

        return res

    """
    dp[i][j][p][q] : whether s2[i..j] is a scramble of s1[p..q] or not, because the length of those two string should be 
    same, so we can use three dimension to show : 
        k : length of the string 
        dp[i][j][k]: whether the s1[i:i+k] is a scramble of s2[j:j+k] or not 
    """
    def isScramble(self, s1: str, s2: str) -> bool:
        length = len(s1)
        dp = [[[False] * (length+1) for _ in range(length)] for _ in range(length)]

        for i in range(length):
            for j in range(length):
                if s1[i] == s2[j]:
                    dp[i][j][1] = True

        for l in range(2, length+1):
            for i in range(length - l+1):
                for j in range(length - l+1):
                    for k in range(1, l):
                        if (dp[i][j][k] and dp[i+k][j+k][l-k]) or (dp[i][j+l-k][k] and dp[i+k][j][l-k]):
                            dp[i][j][l] = True
                            break
        return dp[0][0][-1]