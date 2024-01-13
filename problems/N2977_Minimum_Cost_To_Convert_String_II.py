import collections
import sys
from typing import List

"""
1. Trie
2. DP
3  Shortest path
"""
class TreeNode(object):
    def __init__(self):
        self.arr = [None] * 26
        self.idx = -1

class Solution:
    def minimumCost_(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        original = [word[::-1] for word in original]
        changed = [word[::-1] for word in changed]
        words = set(original + changed)
        mw = collections.defaultdict(int)
        i = 0
        root = TreeNode()

        for word in words:
            mw[word] = i
            i += 1
            cur = root
            for c in word:
                if cur.arr[ord(c) - ord('a')] == None:
                    cur.arr[ord(c) - ord('a')] = TreeNode()
                cur = cur.arr[ord(c) - ord('a')]
            cur.idx = mw[word]

        lmw = len(mw)
        l = len(original)
        dc = [[sys.maxsize] * lmw for _ in range(lmw)]
        for i in range(lmw):
            dc[i][i] = 0
        for i in range(l):
            dc[mw[original[i]]][mw[changed[i]]] = min(dc[mw[original[i]]][mw[changed[i]]], cost[i])

        for k in range(lmw):
            for i in range(lmw):
                for j in range(lmw):
                    dc[i][j] = min(dc[i][j], dc[i][k] + dc[k][j])

        length = len(source)
        source = '#' + source
        target = '#' + target
        dp = [sys.maxsize] * (length + 1)
        dp[0] = 0
        for i in range(1, length + 1):
            if source[i] == target[i]:
                dp[i] = min(dp[i], dp[i - 1])
            s, t = root, root
            for j in range(i, 0, -1):
                if s.arr[ord(source[j]) - ord('a')] == None:
                    break
                s = s.arr[ord(source[j]) - ord('a')]
                if t.arr[ord(target[j]) - ord('a')] == None:
                    break
                t = t.arr[ord(target[j]) - ord('a')]
                if s.idx < 0 or t.idx < 0:
                    continue
                dp[i] = min(dp[i], dp[j-1] + dc[s.idx][t.idx])

        return dp[-1] if dp[-1] != sys.maxsize else -1

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str],
                    cost: List[int]) -> int:
        words = set(original + changed)
        mw = collections.defaultdict(int)
        i = 0
        for word in words:
            mw[word] = i
            i += 1

        lmw = len(mw)
        l = len(original)
        dc = [[sys.maxsize] * lmw for _ in range(lmw)]
        for i in range(lmw):
            dc[i][i] = 0
        for i in range(l):
            dc[mw[original[i]]][mw[changed[i]]] = min(dc[mw[original[i]]][mw[changed[i]]], cost[i])

        for k in range(lmw):
            for i in range(lmw):
                for j in range(lmw):
                    dc[i][j] = min(dc[i][j], dc[i][k] + dc[k][j])

        length = len(source)
        source = '#' + source
        target = '#' + target
        dp = [sys.maxsize] * (length + 1)
        dp[0] = 0
        for i in range(1, length + 1):
            if source[i] == target[i]:
                dp[i] = dp[i-1]
            for j in range(1, i+1):
                ps, pt = source[j:i+1], target[j:i+1]
                if ps not in mw or pt not in mw:
                    continue
                dp[i] = min(dp[i], dc[mw[ps]][mw[pt]] + dp[j-1])
        return dp[-1] if dp[-1] != sys.maxsize else -1








