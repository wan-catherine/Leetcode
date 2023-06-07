import bisect
from typing import List

from sortedcontainers import SortedList


class Solution:
    def minReverseOperations_TLE(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        odds, evens = [], []
        ban = set(banned)
        for i in range(n):
            if i == p:
                continue
            if i in ban:
                continue
            if i % 2:
                odds.append(i)
            else:
                evens.append(i)
        arr = [-1] * n
        arr[p] = 0
        nodes = [(p, 0)]
        while nodes:
            nn = []
            for node, t in nodes:
                l = max(0, node - k + 1)
                rl = l + k - 1
                ll = l - (node - rl)
                r = min(n-1, node + k - 1)
                lr = r - k + 1
                rr = r - (node - lr)

                if ll % 2:
                    li = bisect.bisect_left(odds, ll)
                    remove = set()
                    while li < len(odds) and odds[li] <= rr:
                        arr[odds[li]] = t + 1
                        nn.append((odds[li], t + 1))
                        remove.add(odds[li])
                        li += 1
                    for i in remove:
                        odds.remove(i)
                else:
                    li = bisect.bisect_left(evens, ll)
                    remove = set()
                    while li < len(evens) and evens[li] <= rr:
                        arr[evens[li]] = t + 1
                        nn.append((evens[li], t + 1))
                        remove.add(evens[li])
                        li += 1
                    for i in remove:
                        evens.remove(i)

            nodes = nn
        return arr

    def minReverseOperations(self, n: int, p: int, banned: List[int], K: int) -> List[int]:
        remaining = [SortedList(), SortedList()]
        banned = set(banned)
        for u in range(n):
            if u != p and u not in banned:
                remaining[u & 1].add(u)

        queue = [p]
        dist = [-1] * n
        dist[p] = 0
        for node in queue:
            lo = max(node - K + 1, 0)
            lo = 2 * lo + K - 1 - node
            hi = min(node + K - 1, n - 1) - (K - 1)
            hi = 2 * hi + K - 1 - node

            for nei in list(remaining[lo % 2].irange(lo, hi)):
                queue.append(nei)
                dist[nei] = dist[node] + 1
                remaining[lo % 2].remove(nei)

        return dist

