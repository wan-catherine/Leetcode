class Solution:
    def findNthDigit(self, n: int) -> int:
        if n <= 9:
            return n
        total = 9
        v = 9
        b = 1
        while total < n:
            b += 1
            v *= 10
            total += v * b
        previous = total - v * b
        p = (n - previous - 1) // b
        q = (n - previous - 1) % b
        return int(str(10 ** (b - 1) + p)[q])
