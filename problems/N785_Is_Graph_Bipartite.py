class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        if not graph:
            return False
        self.graph = graph
        graph_len = len(graph)
        self.colors = [0] * graph_len
        for i in range(graph_len):
            if self.colors[i] == 0 and not self.dfs(i, 1):
                return False
        return True

    def dfs(self, vertex, color):
        self.colors[vertex] = color
        for i in self.graph[vertex]:
            if self.colors[i] == color:
                return False
            if self.colors[i] == 0 and not self.dfs(i, -color):
                return False
        return True