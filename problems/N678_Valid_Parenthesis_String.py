class Solution(object):
    """
    left_max is the maximum number of unmatched "(" , treated all '*' as '('
    left_min is the minimum number of unmatched "(", treated all '*' as ')'
    so [left_min, left_max] will the range of all unmatched '('

    if left_max < 0: it means more ")" than "(", so no matter what's next , there is impossible to match them . so return False
    if left_min < 0: it means "*" + ")" more than "(", so we can change "*" -> "(", one change can match two more ")":
        left_min = 0
        stars -= left_min // 2

    """
    def checkValidString_onepass(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stars, left_max, left_min = 0, 0, 0
        for c in s:
            if c == '(':
                left_max += 1
                left_min += 1
            elif c == ')':
                left_max -= 1
                left_min -= 1
            else:
                stars += 1
                left_max += 1
                left_min -= 1

            if left_max < 0:
                return False

            if stars > 0 and left_min < 0:
                if 2 * stars < abs(left_min):
                    return False
                else:
                    left_min = 0
                    stars -= left_min // 2
        return left_min == 0

    """
    DP 
    1. there is only one character : it's true if it's a '*'
    2. there is more than one character : *[****]*, if the leftest is in ["(", "*"] and the rightest is in [")", "*] 
       and the middle substring is also true, the the whole string is true.
    3. if not 1 and not 2, then we will try to split the string into two substrings and check it again. If we find one is true, 
       then we can break and return True, all other are false. 
       
    O(N^3)
    """
    def checkValidString(self, s):
        if not s:
            return True
        length = len(s)
        dp = [[0]*length for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1 if s[i] == '*' else 0

        for distance in range(1, length):
            for i in range(distance, length):
                j = i - distance
                if s[j] in ["(", "*"] and s[i] in [")", "*"]:
                    if i-1 < j+ 1 or dp[i-1][j+1]:
                        dp[i][j] = 1
                        continue
                for k in range(j+1, i):
                    if dp[i][k+1] and dp[k][j]:
                        dp[i][j] = 1
                        break
        return dp[length-1][0]