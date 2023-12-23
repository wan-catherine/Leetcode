import collections
import math
from collections import Counter
from itertools import count

class Solution:
    def beautifulSubstrings_TLE(self, s: str, k: int) -> int:
        length = len(s)
        arr = []
        b = 1
        while True:
            sq = math.sqrt(b * k)
            if sq * 2 > length:
                break
            if int(sq) == sq and sq * 2 <= length:
                arr.append(int(sq))
            b += 1

        prev = [0]
        for i in range(length):
            if s[i] in "aeiou":
                prev.append(prev[-1] + 1)
            else:
                prev.append(prev[-1])
        res = 0
        for i in arr:
            l = 2 * i
            for j in range(l-1, length):
                if prev[j+1] - prev[j - l +1] == i:
                    res += 1
        return res

    def beautifulSubstrings_(self, s: str, k: int) -> int:
        n = len(s)
        l = next(i for i in count(1) if i * i % k == 0) * 2
        vowels = set(list('aeiou'))
        seen = [Counter() for i in range(l)]
        seen[-1][0] = 1
        res = 0
        v = 0
        for i, c in enumerate(s):
            v += 1 if s[i] in vowels else -1
            res += seen[i % l][v]
            seen[i % l][v] += 1
        return res

    def beautifulSubstrings(self, s: str, k: int) -> int:
        def get_prime(n):
            prime = [True for i in range(n + 1)]
            p = 2
            while p * p <= n:
                if prime[p]:
                    for i in range(p * p, n + 1, p):
                        prime[i] = False
                p += 1
            res = []
            for i in range(2, n + 1):
                if prime[i]:
                    res.append(i)
            return res
        primes = get_prime(k)
        m = 1
        for p in primes:
            count = 0
            while k % p == 0:
                count += 1
                k //= p
            if count == 0:
                continue
            if count % 2 == 1:
                m *= pow(p, (count+1)//2)
            else:
                m *= pow(p, count//2)
        m *= 2

        length = len(s)
        s = '#' + s
        res = 0
        status = collections.defaultdict(dict)
        status[0][0] = 1
        count = 0
        sv = set(list("aeiou"))
        for i in range(1, length + 1):
            if s[i] in sv:
                count += 1
            else:
                count -= 1
            if count in status and i%m in status[count]:
                res += status[count][i%m]
            if i%m in status[count]:
                status[count][i%m] += 1
            else:
                status[count][i%m] = 1
        return res



