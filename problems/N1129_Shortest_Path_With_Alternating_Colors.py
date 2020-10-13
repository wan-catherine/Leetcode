import collections


class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        """
        :type n: int
        :type red_edges: List[List[int]]
        :type blue_edges: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(set)
        for src, des in red_edges:
            graph[src].add((des, 1))

        for src, des in blue_edges:
            graph[src].add((des, 2))
        seen = set()

        res = [-1] * n

        # initiate the q for bfs with node (cur Node, distanceTo0, from which color)
        q = [(0, 0, 1), (0, 0, 2)]

        while q:
            nextq = []
            for cur, dist, color in q:
                # shortest distance we get so far
                if res[cur] == -1:
                    res[cur] = dist
                for neighbor, nextColor in graph[cur]:
                    # visit the node with a different color and record the edges we have visited so far
                    if nextColor != color and (cur, neighbor, nextColor) not in seen:
                        nextq.append((neighbor, dist + 1, nextColor))
                        seen.add((cur, neighbor, nextColor))
            q = nextq

        return res

