"""
DP
"""
import math


class Solution(object):
    def numSquares_dp(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * (n+1)
        for i in range(2,n+1):
            j = 1
            while (j+1)*(j+1) < i:
                j += 1
            if (j+1)**2 == i:
                dp[i] = 1
                continue
            minimum = i
            while j > 0:
                minimum = min(minimum, dp[i-j**2]+1)
                j -= 1
            dp[i] = minimum
        return dp[-1]

    """
    https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem
    Any number can be represented as sum of 4 squares. 
    1. if i*i == n, then return 1 
    2. if i*i + j*j == n , then return 2
        use for loop .
    3. Adrien-Marie Legendre extended the theorem in 1797–8 with his three-square theorem, by proving that a positive integer can be expressed as the sum of three squares if and only if it is not of the form {\displaystyle 4^{k}(8m+7)}4^{k}(8m+7) for integers {\displaystyle k}k and {\displaystyle m}m.
        so we check 4^k(8m+7) == n, then return 4
    4. all other return 3.
    """
    def numSquares_math(self, n):
        if int(math.sqrt(n))**2 == n:
            return 1
        for i in range(int(math.sqrt(n)) + 1):
            if int(math.sqrt(n - i*i))**2 == n - i*i:
                return 2

        while n % 4 == 0:
            n //= 4
        if n % 8 == 7:
            return 4
        return 3

    def numSquares_dp(self, n):
        dp = [0]
        while len(dp) <= n:
            dp += min(dp[-i * i] for i in range(1, int(len(dp) ** 0.5 + 1))) + 1,
        return dp[n]

    """
    BFS
    find the shortest path . 
    """
    def numSquares(self, n):
        m = int(math.sqrt(n))
        if m ** 2 == n:
            return 1

        stack = set([n])
        count = 0
        while stack:
            new_stack = set()
            count += 1
            for num in stack:
                for i in range(1, m+1):
                    val = num - i*i
                    if val == 0:
                        return count
                    if val < 0:
                        break
                    new_stack.add(num - i*i)
            stack = new_stack
        return count
