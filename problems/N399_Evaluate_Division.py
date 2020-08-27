import collections


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = collections.defaultdict(set)
        edge_weight_map = collections.defaultdict(float)

        length = len(equations)
        for i in range(length):
            graph[equations[i][0]].add(equations[i][1])
            graph[equations[i][1]].add((equations[i][0]))
            edge_weight_map[tuple(equations[i])] = values[i]
            edge_weight_map[tuple(equations[i][::-1])] = (1/values[i]) if values[i] != 0 else None

        res = []
        for u, v in queries:
            if u not in graph:
                res.append(-1.0)
            elif u == v:
                res.append(1.0)
            elif v in graph[u]:
                res.append(edge_weight_map[(u,v)])
            else:
                res.append(self.dfs(u, v, graph, edge_weight_map, 1, set()))
        return res

    def dfs(self, start, end, graph, edge_weight_map, value, visited):
        if start not in graph:
            return -1.0
        visited.add(start)
        for node in graph[start]:
            if node in visited:
                continue
            val = edge_weight_map[(start, node)] * value
            if node == end:
                return val
            temp = self.dfs(node, end, graph, edge_weight_map, val, visited)
            if temp != -1.0:
                return temp
        return -1.0
