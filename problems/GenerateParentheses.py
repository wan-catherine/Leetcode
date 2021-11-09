from typing import List


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.helper(n, res, "", 0, 0)
        return  res;

    def helper(self,n, res, temp, right, left):
        if left < n:
            self.helper(n, res, temp+"(", right, left + 1)
        if right < left:
            self.helper(n, res, temp+")", right + 1, left)
        if right == n:
            res.append(temp)

    def generateParenthesis_dp_version(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]
    # idea: dynamic programming: dp[0]=''
    # step 1: generate one pair dp[1]= ()
    # step 2: add the second pair either by inserting in () -> (()) or add afterwards ()(). dp[2] = (()), ()()
    # step 3: add the thrid pair either by inserting in ((())), or (())() or ()(()) or ()()().
    # dp[3]=  ((())), (())(), ()(()), ()()(), (()()).
    # how was this done?
    # for i=3 here, j = 0,1,2.
    # For j=0, add all combination of (dp[0])dp[2] = ()(()), ()()().
    # For j=1, add all combination of (dp[1])dp[1] = (())().
    # For j=2, add all combination of (dp[2])dp[0]=((())), (()()).

    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(used, left, cur):
            if used == n and left == 0:
                res.append(''.join(cur[:]))
                return
            if used == n:
                cur.append(')')
                dfs(used, left - 1, cur[:])
            else:
                if left > 0:
                    cur.append(')')
                    dfs(used, left - 1, cur[:])
                    cur.pop()
                if used < n:
                    cur.append('(')
                    dfs(used + 1, left + 1, cur[:])

        dfs(0, 0, [])
        return res
