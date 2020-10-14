import collections


class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        graph = collections.defaultdict(list)

        for i, m in enumerate(manager):
            graph[(m, informTime[m])].append(i)

        def dfs(id, cur):
            if (id, informTime[id]) not in graph:
                return cur
            val = 0
            for i in graph[(id, informTime[id])]:
                val = max(val, dfs(i, cur+informTime[id]))
            return val

        return dfs(headID, 0)
