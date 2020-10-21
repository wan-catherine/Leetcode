class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False

        s1 = '#' + s1
        s2 = '#' + s2
        s3 = '#' + s3

        dp = [[False]* (l2+1) for _ in range(l1+1)]
        for i in range(l1+1):
            if s1[i] == s3[i]:
                dp[i][0] = True
            else:
                break
        for i in range(l2+1):
            if s2[i] == s3[i]:
                dp[0][i] = True
            else:
                break

        """
        Here notice how to write the if clause. 
        Key point : 
            s1[i] == s3[i+j] and s2[j] == s3[i+j] can be true at the same time!!!
            if it writes like this : 
                if s1[i] == s3[i+j]:
                    dp[i][j] = dp[i-1][j]
                elif s2[j] == s3[i+j] :
                    dp[i][j] = dp[i][j-1]
            It will be wrong. 
            when s2[j] == s3[i+j] and dp[i][j-1] == True, dp[i][j] should be True. 
            But here , it will go to the if clause and set as False, then ignore the elif clause . 
        """
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                # if s1[i] == s3[i+j]:
                #     dp[i][j] = dp[i][j] or dp[i-1][j]
                # if s2[j] == s3[i+j] :
                #     dp[i][j] = dp[i][j] or dp[i][j-1]
                if s1[i] == s3[i+j] and dp[i-1][j]:
                    dp[i][j] = True
                elif s2[j] == s3[i+j] and dp[i][j-1]:
                    dp[i][j] = True
        print(dp)
        return dp[-1][-1]