import collections
import math
"""
Key part : 
1 <= nums[i] <= 50
so we can have a records which key : num , value : all ancestor's depth.
this way, we can loop 1-50 instead of loop all ancestors .
"""

class Solution(object):
    def getCoprimes(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        length = len(nums)
        visited = [0] * length
        res = [-1] * length
        path = []
        records = [[] for _ in range(51)]
        def dfs(index, depth):
            if visited[index]:
                return
            visited[index] = 1
            i = -1
            for d in range(1, 51):
                if records[d] and math.gcd(nums[index], d) == 1:
                    i = max(i, records[d][-1])
            res[index] = path[i] if i != -1 else -1

            for nxt in graph[index]:
                if visited[nxt]:
                    continue
                path.append(index)
                records[nums[index]].append(depth)
                dfs(nxt, depth+1)
                path.pop()
                records[nums[index]].pop()
        dfs(0, 0)
        return res

