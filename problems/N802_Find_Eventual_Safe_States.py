class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        status = [0]*n
        def dfs(node):
            if status[node] == 1:
                return True
            if status[node] == 0:
                status[node] = 1

            for i in graph[node]:
                if status[i] == 2:
                    continue
                if dfs(i):
                    return True
            status[node] = 2
            return False

        for i in range(n):
            if status[i] == 0:
                dfs(i)

        return [i for i in range(n) if status[i] == 2]

