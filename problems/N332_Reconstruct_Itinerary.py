import collections


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = collections.defaultdict(list)
        visited = collections.defaultdict(int)
        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])
            visited[(ticket[0], ticket[1])] += 1
        self.length = len(tickets) + 1
        for key in graph:
            graph[key].sort()

        res = self.dfs(graph, 'JFK', [], visited)
        return res

    def dfs(self, graph, start, arr, visited):
        arr.append(start)
        if start not in graph:
            return
        for end in graph[start]:
            if not visited[(start, end)]:
                continue
            visited[(start, end)] -= 1
            self.dfs(graph, end, arr, visited)
            if len(arr) == self.length:
                return arr
            visited[(start, end)] += 1
            arr.pop()

