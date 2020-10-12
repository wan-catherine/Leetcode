import collections

class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        length = len(quiet)
        graph = collections.defaultdict(list)
        for u, v in richer:
            graph[v].append(u)

        res = [-1]*length
        memo = {}
        def dfs(n):
            if n in memo:
                return memo[n]
            p = quiet[n]
            for i in graph[n]:
                p = min(p, dfs(i))
            memo[n] = p
            return p

        people = {}
        for i in range(length):
            if i not in graph:
                res[i] = i
                continue
            q = dfs(i)
            if q in people:
                res[i] = people[q]
                continue
            for index, v in enumerate(quiet):
                if q == v:
                    people[q] = index
                    res[i] = index
                    break
        return res

