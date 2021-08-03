import collections
from typing import List

"""
1. How to pick a from an array so that maximizes a ^ b ==> LC 421
2. DFS, solve queries when traversing the tree , dynamic add/delete nodes in trie tree
3. How to deal with backtracking when DFS for trie (deleting nodes in Trie) ==> LC 21 
"""

class Trie:
    def __init__(self):
        self.next = [None, None]
        self.cnt = 0

class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        mq = collections.defaultdict(list)
        for idx, li in enumerate(queries):
            mq[li[0]].append((idx, li[1]))
        children = collections.defaultdict(list)
        top = None
        for idx, p in enumerate(parents):
            if p == -1:
                top = idx
            else:
                children[p].append(idx)
        length = len(queries)
        res = [0] * length
        root = Trie()
        def dfs(val):
            cur = root
            for i in range(31, -1, -1):
                d = (val >> i) & 1
                if not cur.next[d]:
                    cur.next[d] = Trie()
                cur = cur.next[d]
                cur.cnt += 1
            for idx, v in mq[val]:
                ans = 0
                cur = root
                for i in range(31, -1, -1):
                    ans = ans * 2
                    d = (v >> i) & 1
                    # here must check cur.next[1-d].cnt, not cur.cnt
                    if not cur.next[1-d] or cur.next[1-d].cnt == 0:
                        cur = cur.next[d]
                        ans += d
                    else:
                        cur = cur.next[1-d]
                        ans += 1 - d
                res[idx] = v ^ ans

            for child in children[val]:
                dfs(child)

            cur = root
            for i in range(31, -1, -1):
                d = (val >> i) & 1
                cur = cur.next[d]
                cur.cnt -= 1
        dfs(top)
        return res