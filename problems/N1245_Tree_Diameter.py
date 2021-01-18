"""
Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.
The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v. 
Each node has labels in the set {0, 1, ..., edges.length}.

Example 1:
Input: edges = [[0,1],[0,2]]
Output: 2
Explanation:
A longest path of the tree is the path 1 - 0 - 2.

Example 2:
Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
Output: 4
Explanation:
A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.
 
Constraints:
0 <= edges.length < 10^4
edges[i][0] != edges[i][1]
0 <= edges[i][j] <= edges.length
The given edges form an undirected tree.
"""
import collections
"""
Twice dfs:
first : use any node (a) to search the farest node from a which is b 
second : use b to search the farest node from b which is c 
the answer is the path between b and c

Here we also can use bfs
"""

class Solution(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        length = len(edges)
        def dfs(node, cur):
            visited[node] = 1
            maxlen, ans = 0, None
            for n in graph[node]:
                if n == node:
                    continue
                if visited[n]:
                    continue
                node, l = dfs(n, cur+1)
                if l > maxlen:
                    maxlen = l
                    ans = node
            if not ans:
                return (node, cur)
            return (ans, maxlen)

        visited = [0] * (length+1)
        left, _ = dfs(0, 0)
        visited = [0] * (length + 1)
        right, res = dfs(left, 0)
        return res


