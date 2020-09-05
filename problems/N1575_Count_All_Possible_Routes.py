import collections


class Solution(object):
    def countRoutes(self, locations, start, finish, fuel):
        """
        :type locations: List[int]
        :type start: int
        :type finish: int
        :type fuel: int
        :rtype: int
        """
        graph = collections.defaultdict(list)
        length = len(locations)
        self.memo = {}
        for i in range(length):
            for j in range(length):
                if i == j:
                    continue
                graph[i].append((j, abs(locations[i] - locations[j])))
        self.finish = finish
        self.start = start
        self.helper(graph, finish, fuel)
        print(self.memo)
        return self.memo[(finish, fuel)] % (10**9 + 7)

    def helper(self, graph, current, fuel):
        if (current, fuel) in self.memo:
            return self.memo[(current, fuel)]
        # if fuel < 0:
        #     return 0
        value = 0
        if current == self.start:
            value += 1

        for v, w in graph[current]:
            if fuel < w:  #this is the key part to stop the recursion.
                continue
            value += self.helper(graph, v, fuel-w)
        self.memo[(current, fuel)] = value
        return value

