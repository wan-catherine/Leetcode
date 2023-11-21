import collections
from typing import List


class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        def get_prime(n):
            prime = [True for i in range(n + 1)]
            p = 2
            while p * p <= n:
                if prime[p]:
                    for i in range(p * p, n + 1, p):
                        prime[i] = False
                p += 1
            res = set()
            for i in range(2, n + 1):
                if prime[i]:
                    res.add(i)
            return res
        primes = get_prime(n)

        parents = [i for i in range(n + 1)]
        sizes = [1] * (n + 1)

        def find(x):
            while x != parents[x]:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x

        def union(p, q):
            if sizes[p] < sizes[q]:
                parents[p] = q
                sizes[q] += sizes[p]
            else:
                parents[q] = p
                sizes[p] += sizes[q]

        def is_prime(a):
            return a in primes

        count = [0] * (n + 1)
        grid = collections.defaultdict(list)
        for u, v in edges:
            grid[u].append(v)
            grid[v].append(u)
            if not is_prime(u) and not is_prime(v):
                p, q = find(u), find(v)
                if p == q:
                    continue
                union(p, q)

        for i in range(n+1):
            count[find(i)] += 1

        res = 0
        for p in primes:
            arr = []
            for nxt in grid[p]:
                if not is_prime(nxt):
                    arr.append(count[find(nxt)])
            total = sum(arr)
            ans = 0
            for x in arr:
                ans += x * (total - x)
            res += ans // 2 + total
        return res

