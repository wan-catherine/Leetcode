from typing import List


class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x : (x[1], x[0]))
        visited = [0] * 2001
        ps, pe = tasks[0][0], tasks[0][1]
        for s, e, c in tasks:
            l, r = s, pe
            for i in range(l, r + 1):
                if visited[i] == 1:
                    c -= 1
                    if c == 0:
                        break
            idx = e
            while c > 0:
                if visited[idx] == 0:
                    visited[idx] = 1
                    c -= 1
                idx -= 1

            ps, pe = s, e
        return sum(visited)

