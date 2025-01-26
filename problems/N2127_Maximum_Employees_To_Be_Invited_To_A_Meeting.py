import collections
from typing import List

"""
1. a circle larger than 2 , then all node in the circle can be on the table (maximum)
2. a circle has size as 2:
    a. then two linklist of each node can be on the table 
    b. each 2 size circel can be on the table (sum)
"""
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        length = len(favorite)
        indegree = collections.defaultdict(int)
        for i in range(length):
            indegree[favorite[i]] += 1

        visited = [0] * length
        depth = [1] * length
        stack = []
        for i in range(length):
            if indegree[i] == 0:
                stack.append(i)
                visited[i] = 1
                depth[i] = 1

        while stack:
            nstack = []
            for idx in stack:
                nxt = favorite[idx]
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    nstack.append(nxt)
                    visited[nxt] = 1
                depth[nxt] = depth[idx] + 1
            stack = nstack

        circle, link = 0, 0
        for i in range(length):
            if visited[i] == 1:
                continue
            idx = i
            count = 0
            while visited[idx] == 0:
                count += 1
                visited[idx] = 1
                idx = favorite[idx]

            if count > 2:
                circle = max(circle, count)
            elif count == 2:
                link += depth[i] + depth[favorite[i]]

        return max(circle, link)
