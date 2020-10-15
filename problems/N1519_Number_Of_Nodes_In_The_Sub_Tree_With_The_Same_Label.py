import collections


class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        res = [0]*n
        def dfs(i):
            visited.add(i)
            ans = [0] * 26
            for j in graph[i]:
                if j in visited:
                    continue
                r = dfs(j)
                for k, v in enumerate(r):
                    ans[k] += v

            index = ord(labels[i]) - ord('a')
            ans[index] += 1
            res[i] = ans[index]
            return ans[:]
        dfs(0)
        return res
