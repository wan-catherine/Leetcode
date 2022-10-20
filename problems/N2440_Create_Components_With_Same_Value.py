import collections
from collections import deque
from typing import List


class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        if not edges:
            return 0
        length, total = len(nums), sum(nums)
        graph = collections.defaultdict(list)
        indegrees = [0] * length
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegrees[u] += 1
            indegrees[v] += 1

        leaves = [i for i in range(length) if indegrees[i] == 1]

        def check(val):
            visited = [0] * length
            status = [i for i in nums]
            idg = indegrees[:]
            pq = deque(leaves)
            while pq:
                node = pq.popleft()
                visited[node] = 1
                if status[node] > val:
                    return False
                if status[node] == val:
                    status[node] = 0
                for nxt in graph[node]:
                    if visited[nxt]:
                        continue
                    idg[nxt] -= 1
                    status[nxt] += status[node]
                    if idg[nxt] == 1:
                        pq.append(nxt)
            return True

        flag = False
        val = -1
        for i in range(length, -1, -1):
            if total % i:
                continue
            val = total // i
            if check(val):
                flag = True
                break
        if flag:
            return total // val - 1
        return 0



