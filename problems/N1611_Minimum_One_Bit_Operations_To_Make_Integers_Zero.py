"""
1 -> 0 needs 1 operation,
2 -> 0 needs 3 operations,
4 -> 0 needs 7 operations,
2^k needs 2^(k+1)-1 operations.

1XXXXXX -> 1100000 -> 100000 -> 0

1XXXXXX -> 1100000 needs minimumOneBitOperations(1XXXXXX ^ 1100000),
because it needs same operations 1XXXXXX ^ 1100000 -> 1100000 ^ 1100000 = 0.

1100000 -> 100000 needs 1 operation.
100000 -> 0, where 100000 is 2^k, needs 2^(k+1) - 1 operations.

In total,
f(n) = f((b >> 1) ^ b ^ n) + 1 + b - 1,
where b is the maximum power of 2 that small or equals to n.
"""

class Solution(object):
    def minimumOneBitOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(n):
            if n not in dp:
                b = 1
                while (b << 1) <= n:
                    b = b << 1
                dp[n] = self.minimumOneBitOperations((b >> 1) ^ b ^ n) + 1 + b - 1
            return dp[n]

        dp = {0: 0}
        return helper(n)