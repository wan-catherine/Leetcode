import collections
"""
See : https://leetcode.com/problems/sum-of-distances-in-tree/discuss/130583/C%2B%2BJavaPython-Pre-order-and-Post-order-DFS-O(N)

Explanation
Let's solve it with node 0 as root.

Initial an array of hashset tree, tree[i] contains all connected nodes to i.
Initial an array count, count[i] counts all nodes in the subtree i.
Initial an array of res, res[i] counts sum of distance in subtree i.

Post order dfs traversal, update count and res:
count[root] = sum(count[i]) + 1
res[root] = sum(res[i]) + sum(count[i])

Pre order dfs traversal, update res:
When we move our root from parent to its child i, count[i] points get 1 closer to root, n - count[i] nodes get 1 futhur to root.
res[i] = res[root] - count[i] + N - count[i]

return res, done.


Several key points :
1. how to find the relationship between res[parent], res[child] 
2. how to find all count[i] which means i as root tree , how many nodes this tree has. Need to use post order .
3. how to update res . Need to use pre order . We find know the parent's result, then we can calculate it's children.

"""

class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = [1]*N
        res = [0]*N

        def post_traversal(current, parent):
            for next in graph[current]:
                if next == parent:
                    continue
                post_traversal(next, current)
                count[current] += count[next]
                res[current] += res[next] + count[next]

        def pre_traversal(current, parent):
            for next in graph[current]:
                if next == parent:
                    continue
                res[next] = res[current] - count[next] + N - count[next]
                pre_traversal(next, current)

        post_traversal(0, -1)
        pre_traversal(0, -1)
        return res
