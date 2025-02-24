import collections
import sys
from typing import List


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = collections.defaultdict(list)
        for k, v in edges:
            graph[k].append(v)
            graph[v].append(k)
        leaves = set()
        for k, li in graph.items():
            if len(li) == 1 and k != 0:
                leaves.add(k)
        status = {bob:0}
        def dfs(idx, pre, step):
            if idx == 0:
                status[idx] = step
                return True
            for nxt in graph[idx]:
                if nxt == pre:
                    continue
                status[nxt] = step + 1
                if dfs(nxt, idx, step + 1):
                    return True
                del status[nxt]
            return False
        dfs(bob, None, 0)

        res = -sys.maxsize
        def dfsa(idx, pre, cur, step):
            nonlocal res
            if idx in leaves:
                res = max(res, cur)
                return
            step += 1
            for nxt in graph[idx]:
                if nxt == pre:
                    continue
                if nxt in status:
                    if step == status[nxt]:
                        cur += amount[nxt] // 2
                    elif step < status[nxt]:
                        cur += amount[nxt]
                else:
                    cur += amount[nxt]
                dfsa(nxt, idx, cur, step)
                if nxt in status:
                    if step == status[nxt]:
                        cur -= amount[nxt] // 2
                    elif step < status[nxt]:
                        cur -= amount[nxt]
                else:
                    cur -= amount[nxt]
            return
        dfsa(0, None, amount[0], 0)
        return res