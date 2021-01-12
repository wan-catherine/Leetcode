import collections
"""
Basic idea : 
    Find the root which has the connections with all other nodes. 
    if we can't find root, then it won't be construct to a tree, return 0. 
    if we can find one root, then remove this from the graph and check this logic all again. 
    if we can find two roots, then remove one of the root and check this logic all again. 
    
Here, when we find two roots, we can't directly return 2. We need to make sure all sub-nodes can construct a tree first. 
So put the return 2 after solve the sub-problems. 
"""

class Solution(object):
    def checkWays(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        graph = collections.defaultdict(set)
        for u, v in pairs:
            graph[u].add(v)
            graph[v].add(u)

        def helper(nodes):
            roots = []
            length = len(nodes)
            for node in graph.keys():
                if node not in nodes:
                    continue
                if len(graph[node]) + 1 == length:
                    roots.append(node)
            if not roots:
                return 0
            root = roots[0]

            del graph[root]
            nodes.remove(root)
            keys = list(graph.keys())
            for key in keys:
                if key not in nodes:
                    continue
                graph[key].remove(root)
                if len(graph[key]) == 0:
                    del graph[key]
                    nodes.remove(key)
            if not graph:
                return len(roots)
            # get groups
            comps, visited, i = collections.defaultdict(set), set(), 0
            def dfs(node, i):
                comps[i].add(node)
                visited.add(node)
                for neib in graph[node]:
                    if neib not in visited:
                        dfs(neib, i)

            for node in nodes:
                if node not in visited:
                    dfs(node, i)
                    i += 1

            ans = [helper(comps[i]) for i in comps]
            if 0 in ans:
                return 0
            if 2 in ans:
                return 2
            # must after all sub comps checked !!!
            if len(roots) > 1:
                return 2
            return 1

        return helper(set(graph.keys()))

