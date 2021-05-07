class Solution:
    """
    Factorial value : n!
    2*5 = 10 will add one zero , so we need to calculate the number of 2 and 5.
    and 2 always more than 5, so we only count 5.
    """
    def trailingZeroes(self, n: int) -> int:
        res = 0
        i = 1
        while 5 ** i <= n:
            res += n // (5 ** i)
            i += 1
        return res