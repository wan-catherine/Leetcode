class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dp = [False] * (n + 1)
        dp[1] = True

        for i in range(2, n + 1):
            k = 1
            maximum = int(i**0.5) + 1
            while k <= maximum:
                square = k ** 2
                if square > i:
                    break
                if square == i:
                    dp[i] = True
                    break

                dp[i] = dp[i] or (not dp[i - square ])
                k += 1

        return dp[-1]