import collections
from typing import List


class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        total = (m - 1) * (n - 1)
        mapping = collections.defaultdict(int)
        blocks = set((i,j) for i, j in coordinates)
        direction = [(-1,-1), (-1,0), (0,-1), (0, 0)]
        res = collections.defaultdict(int)
        for u, v in coordinates:
            for i, j in direction:
                lr, lc = u + i, v + j
                rr, rc = lr + 1, lc + 1
                if lr < 0 or lr >= m or lc < 0 or lc >= n or rr < 0 or rr >= m or rc < 0 or rc >= n or (lr,lc) in mapping:
                    continue
                count = 0
                for p in range(lr, rr + 1):
                    for q in range(lc , rc + 1):
                        if (p, q) in blocks:
                            count += 1
                mapping[(lr, lc)] = count
                res[count] += 1

        return [total - sum(res.values()), res[1], res[2], res[3], res[4]]
