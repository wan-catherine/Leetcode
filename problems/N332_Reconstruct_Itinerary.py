import collections


class Solution(object):
    def findItinerary_before(self, tickets):
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

        res = self.dfs_before(graph, 'JFK', [], visited)
        return res

    def dfs_before(self, graph, start, arr, visited):
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

    def findItinerary(self, tickets):
        if not tickets:
            return None
        self.length = len(tickets)
        self.graph = collections.defaultdict(list)
        self.visited = collections.defaultdict(int)
        for f, t in tickets:
            self.graph[f].append(t)
            self.visited[(f,t)] += 1
        res = ['JFK']
        self.dfs('JFK', res, 0)
        return res


    def dfs(self, f, res, count):
        if f not in self.graph:
            return

        for t in sorted(self.graph[f]):
            if not self.visited[(f,t)]:
                continue
            self.visited[(f,t)] -= 1
            res.append(t)
            count += 1
            self.dfs(t, res, count)
            if len(res) == self.length + 1:
                return

            res.pop()
            self.visited[(f,t)] += 1

    def findItinerary(self, tickets):
        graph = collections.defaultdict(list)
        deg_out = collections.defaultdict(int)

        # construct adjency list
        for frm, to in tickets:
            graph[frm].append(to)
            deg_out[frm] += 1

        path = []
        for k, v in graph.items():
            graph[k] = sorted(v, reverse=True)

        def dfs(node):
            while graph[node]:
                curr = graph[node].pop()
                dfs(curr)
            path.append(node)

        dfs("JFK")
        return reversed(path)







