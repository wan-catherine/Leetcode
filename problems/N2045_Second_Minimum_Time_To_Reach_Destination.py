import collections
import heapq
from typing import List


class Solution:
    def secondMinimum_TLE(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        stack = [(0, 1)]
        first, second = None, None
        while stack:
            num, node = heapq.heappop(stack)
            if node == n:
                if not first:
                    first = num
                elif not second or second == first:
                    second = num
                else:
                    break
            for nxt in graph[node]:
                heapq.heappush(stack, (num+1, nxt))
        if not second:
            second = first + 2
        res = 0
        flag = 'Green'
        while second:
            if flag == 'Green':
                res += time
                t = res // change
                if t % 2:
                    flag = 'Red'
                second -= 1
            else:
                t = res % change
                res += change - t
                flag = 'Green'
        return res

    def secondMinimum_myself(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        stack = [1]
        step = 0
        visited = [0] * (n + 1)
        visited[1] = 1
        # key part is here
        dist = [0] * (n + 1)
        first, second = None, None
        flag = False
        while stack:
            new_stack = []
            step += 1
            for node in stack:
                if node == n:
                    if first is None:
                        first = step - 1
                    elif second is None or second == first:
                        second = step - 1
                    else:
                        flag = True
                        break
                for nxt in graph[node]:
                    # we need two conditions here !!!
                    # if only use visited[nxt] < 2 , then all different will be connect to nxt, wrong logic.
                    # but adding dist[nxt] < step, so the same level will be ignore.
                    if visited[nxt] < 2 and dist[nxt] < step:
                        visited[nxt] += 1
                        dist[nxt] = step
                        new_stack.append(nxt)
            if flag:
                break

            stack = new_stack
        res = 0
        flag = 'Green'
        while second:
            if flag == 'Green':
                res += time
                t = res // change
                if t % 2:
                    flag = 'Red'
                second -= 1
            else:
                t = res % change
                res += change - t
                flag = 'Green'
        return res

    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [0] * (n + 1)
        dist = [0] * (n + 1)
        stack = [(1, 0)]
        while stack:
            new_stack = []
            for node, t in stack:
                round = t // change
                if round % 2:
                    tt = (round + 1) * change + time
                else:
                    tt = t + time
                for nxt in graph[node]:
                    if visited[nxt] < 2 and dist[nxt] < tt:
                        dist[nxt] = tt
                        visited[nxt] += 1
                        new_stack.append((nxt, tt))
                        if visited[nxt] == 2 and nxt == n:
                            return tt
            stack = new_stack
