class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        MOD = 10 ** 9 + 7
        an, bn = a >> n, b >> n
        if an < bn:
            return self.maximumXorProduct(b, a, n)

        if an > bn:
            for i in range(n-1,-1,-1):
                if a & (1 << i) == b & (1 << i):
                    a = a | (1 << i)
                    b = b | (1 << i)
                else:
                    a = a - (a & (1 << i))
                    b = b | (1 << i)
        else:
            first = True
            for i in range(n-1,-1,-1):
                if a & (1 << i) == b & (1 << i):
                    a = a | (1 << i)
                    b = b | (1 << i)
                else:
                    if first:
                        first = False
                        a = a | (1 << i)
                        b = b - (b & (1 << i))
                    else:
                        a = a - (a & (1 << i))
                        b = b | (1 << i)
        return (a % MOD) * (b % MOD) % MOD

