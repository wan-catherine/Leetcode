import collections
"""
Key point:
    There are two levels of topological sort:
        1. in the group
        2. between the groups
"""
class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """
        group_items = collections.defaultdict(set)
        next_group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = next_group_id
                next_group_id += 1
            group_items[group[i]].add(i)

        def topological_sort(nodes, graph, indegrees, res):
            zeroes = [i for i in nodes if indegrees[i] == 0]
            while zeroes:
                new_zeroes = []
                for i in zeroes:
                    res.append(i)
                    for j in graph[i]:
                        indegrees[j] -= 1
                        if indegrees[j] == 0:
                            new_zeroes.append(j)
                zeroes = new_zeroes
            return len(nodes) == len(res)

        # topological sort in each group
        graph = collections.defaultdict(set)
        indegrees = collections.defaultdict(int)
        for i in range(n):
            for j in beforeItems[i]:
                if group[j] != group[i]:
                    continue
                graph[j].add(i)
                indegrees[i] += 1

        group_items_order = collections.defaultdict(list)
        for gid in group_items.keys():
            nodes = group_items[gid]
            if not topological_sort(nodes, graph, indegrees, group_items_order[gid]):
                return []

        # topological sort between groups
        group_graph = collections.defaultdict(set)
        group_indegrees = collections.defaultdict(int)
        for i in range(n):
            for j in beforeItems[i]:
                if group[j] == group[i]:
                    continue
                if group[i] not in group_graph[group[j]]:
                    group_graph[group[j]].add(group[i])
                    group_indegrees[group[i]] += 1
        group_res = []
        if not topological_sort(group_items.keys(), group_graph, group_indegrees, group_res):
            return []
        ans = []
        for gid in group_res:
            ans.extend(group_items_order[gid])
        return ans





