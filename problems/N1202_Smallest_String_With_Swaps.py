import collections

"""
Use DFS for graph, first , create graph!!!
"""
class Solution(object):
    def smallestStringWithSwaps_dfs(self, s, pairs):
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

    def smallestStringWithSwaps(self, s: str, pairs) -> str:
        length = len(s)
        parents = [i for i in range(length)]
        sizes = [1] * length

        def find(x):
            while x != parents[x]:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x

        def union(p, q):
            pp, pq = find(p), find(q)
            if pp == pq:
                return
            if sizes[pp] < sizes[pq]:
                parents[pp] = pq
            else:
                parents[pq] = pp

        for u, v in pairs:
            union(u, v)

        mapping = collections.defaultdict(list)
        for i in range(length):
            mapping[find(i)].append(s[i])

        # here reverse the array, then pop it one by one
        for gid in mapping.keys():
            mapping[gid].sort(reverse=True)

        res = []
        for i in range(length):
            gid = find(i)
            res.append(mapping[gid].pop())
        return ''.join(res)







