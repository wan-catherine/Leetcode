from typing import List

"""
Find the shortest path problem, then we can think of BFS. 
But this problem, it might visit nodes multiple times, so not like common BFS, we can only check if the 
node is visited or not to remove duplication. 

so we use (state, node) to do the filter. 
if next node is x, and (state_x, x) already visited, then remove it. 

"""

class Solution:
    def shortestPathLength_array_TLE(self, graph: List[List[int]]) -> int:
        length = len(graph)
        visited = [[0] * (2 ** length) for _ in range(length)]
        step = -1
        queue = []
        final = 2 ** length - 1
        for i in range(length):
            queue.append((i, 1 << i))

        while queue:
            new_queue = []
            step += 1
            for i, state in queue:
                visited[i][state] = 1
                if state == final:
                    return step
                for nxt in graph[i]:
                    new_state = state | (1 << nxt)
                    if visited[nxt][new_state]:
                        continue
                    new_queue.append((nxt, new_state))
            queue = new_queue
        return step

    """
    use dictionary faster than use array here .
    """
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        length = len(graph)
        step, final = 0, 2 ** length - 1
        queue = [(i, 1 << i) for i in range(length)]
        memo = set(queue)
        while queue:
            new_queue = []
            for i, state in queue:
                if state == final:
                    return step
                for nxt in graph[i]:
                    new_state = state | (1 << nxt)
                    if (nxt, new_state) in memo:
                        continue
                    new_queue.append((nxt, new_state))
                    memo.add((nxt, new_state))
            step += 1
            queue = new_queue
        return step
