from math import factorial


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        palins = set()
        base = 10 ** ((n - 1) // 2)
        skip = 1 if n % 2 else 0

        for i in range(base, base * 10):
            s = str(i)
            s += s[::-1][skip:]
            ii = int(s)
            if ii % k == 0:
                palins.add("".join(sorted(s)))

        res = 0
        for s in palins:
            count = [0] * 10
            for c in s:
                count[int(c)] += 1
            total = (n - count[0]) * factorial(n - 1)
            for x  in count:
                total //= factorial(x)
            res += total
        return res