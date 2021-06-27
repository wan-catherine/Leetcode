from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        routes = [set(li) for li in routes]
        length = len(routes)
        visited = [0] * length
        stack = set()
        res = 1
        for i, li in enumerate(routes):
            if source in li:
                stack.update(li)
                visited[i] = 1
        if target in stack:
            return res
        while stack:
            if target in stack:
                return res
            new_stack = set()
            for i in range(length):
                if visited[i]:
                    continue
                if stack.intersection(routes[i]):
                    new_stack.update(routes[i])
                    visited[i] = 1
            if not new_stack:
                return -1
            res += 1
            new_stack.update(stack)
            stack = new_stack
        return res if res > 1 else -1
