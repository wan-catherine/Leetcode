import collections
from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        length = len(nums)
        parents = [i for i in range(length)]

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(p, q):
            pp, pq = find(p), find(q)
            if pp == pq:
                return
            parents[pp] = pq

        pn = [(nums[i], i) for i in range(length)]
        pn.sort()
        for i in range(1, length):
            if pn[i][0] - pn[i-1][0] <= limit:
                union(pn[i][1], pn[i-1][1])

        res = [0] * length
        sp = collections.defaultdict(list)
        for i in range(length):
            sp[find(parents[i])].append(i)

        for k, li in sp.items():
            arr = []
            for idx in li:
                arr.append(nums[idx])
            arr.sort()
            i = 0
            for idx in li:
                res[idx] = arr[i]
                i += 1
        return res





