import collections
class Solution:
    def all_topological_sorts(self, num_vertices, connections):
        self.graph = collections.defaultdict(set)
        self.indegree = collections.defaultdict(int)

        for u, v in connections:
            self.graph[u].add(v)
            self.indegree[v] += 1

        self.visited = [0]*num_vertices
        self.n = num_vertices
        res = []
        self.backtracking([], 0, res)
        print(res)

    def backtracking(self, temp, count, res):
        if count == self.n:
            res.append(temp[:])
            return

        for i in range(self.n):
            if self.visited[i] or self.indegree[i]:
                continue
            temp.append(i)
            count += 1
            self.visited[i] = 1
            for j in self.graph[i]:
                self.indegree[j] -= 1

            self.backtracking(temp, count, res)

            self.visited[i] = 0
            for j in self.graph[i]:
                self.indegree[j] += 1
            temp.pop()
            count -= 1

solution = Solution()
solution.all_topological_sorts(6, [[5,2], [5,0], [4,0], [4,1], [2,3], [3,1]])