import collections
from typing import List


class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        length = len(parent)
        tree = [[] for _ in range(length)]
        for i in range(1, length):
            tree[parent[i]].append(i)
        mask = [1 << (ord(c) - ord('a')) for c in s]

        res = 0
        cnt = collections.defaultdict(int)
        cnt[0] = 1

        def dfs(idx, current):
            nonlocal res
            for child in tree[idx]:
                nmask = current ^ mask[child]
                res += cnt[nmask]
                for i in range(26):
                    res += cnt[nmask ^ (1 << i)]
                cnt[nmask] += 1
                dfs(child, nmask)

        dfs(0, 0)
        return res

