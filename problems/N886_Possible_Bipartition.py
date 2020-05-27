class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        # create graph
        self.graph = [[] for i in range(N+1)]
        for li in dislikes:
            self.graph[li[0]].append(li[1])
            self.graph[li[1]].append(li[0])

        # graph coloring
        self.colors = [0] * (N+1)

        for i in range(1, N+1):
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

