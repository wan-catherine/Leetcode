class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def helper(n, k, prefix):
            if k == 0:
                return prefix

            start = 1 if prefix == 0 else 0
            for i in range(start, 10):
                count = totalCountWith(n, prefix * 10 + i) + 1
                if k > count:
                    k -= count
                else:
                    return helper(n, k - 1, prefix * 10 + i)

        def totalCountWith(n, prefix):
            exp = 10
            res = 0
            while True:
                low, high = prefix * exp, prefix * exp + exp - 1
                if low > n:
                    break
                if high < n:
                    res += exp
                else:
                    res += n - low + 1
                    break
                exp *= 10
            return res

        return helper(n, k, 0)

