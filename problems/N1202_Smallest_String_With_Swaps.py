import collections

"""
Use DFS for graph, first , create graph!!!
"""
class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        if not pairs:
            return s

        graph = collections.defaultdict(list)
        for pair in pairs:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])

        visited = [0] * len(s)
        components = []
        for v in graph:
            if visited[v]:
                continue
            com = set()
            self.dfs(graph, v, visited, com)
            components.append(com)

        print (components)
        res = list(s)
        for component in components:
            substr = []
            indexes = []
            for index in component:
                substr.append(s[index])
                indexes.append(index)
            substr.sort()
            indexes.sort()
            i = 0
            for index in indexes:
                res[index]  = substr[i]
                i += 1
        return ''.join(res)

    def dfs(self, graph, node, visited, com):
        if visited[node]:
            return
        visited[node] = 1
        com.add(node)
        for v in graph[node]:
            self.dfs(graph, v, visited, com )







