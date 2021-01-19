"""
An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi.
Note that there may be multiple edges between two nodes, and the graph may not be connected.

Implement the DistanceLimitedPathsExist class:
    DistanceLimitedPathsExist(int n, int[][] edgeList) :  Initializes the class with an undirected graph.
    boolean query(int p, int q, int limit) :
        Returns true if there exists a path from p to q such that each edge on the path has a distance strictly less than limit,
        and otherwise false.
 
Example 1:
Input
    ["DistanceLimitedPathsExist", "query", "query", "query", "query"]
    [[6, [[0, 2, 4], [0, 3, 2], [1, 2, 3], [2, 3, 1], [4, 5, 5]]], [2, 3, 2], [1, 3, 3], [2, 0, 3], [0, 5, 6]]
Output
    [null, true, false, true, false]

Explanation
    DistanceLimitedPathsExist distanceLimitedPathsExist = new DistanceLimitedPathsExist(6, [[0, 2, 4], [0, 3, 2], [1, 2, 3], [2, 3, 1], [4, 5, 5]]);
    distanceLimitedPathsExist.query(2, 3, 2); // return true. There is an edge from 2 to 3 of distance 1, which is less than 2.
    distanceLimitedPathsExist.query(1, 3, 3); // return false. There is no way to go from 1 to 3 with distances strictly less than 3.
    distanceLimitedPathsExist.query(2, 0, 3); // return true. There is a way to go from 2 to 0 with distance < 3: travel from 2 to 3 to 0.
    distanceLimitedPathsExist.query(0, 5, 6); // return false. There are no paths from 0 to 5.
 
Constraints:
    2 <= n <= 10**4
    0 <= edgeList.length <= 10**4
    edgeList[i].length == 3
    0 <= ui, vi, p, q <= n-1
    ui != vi
    p != q
    1 <= disi, limit <= 109
    At most 10**4 calls will be made to query.
"""
class DistanceLimitedPathsExist(object):

    def __init__(self, n, edgeList):
        """
        :type n: int
        :type edgeList: List[List[int]]
        """
        self.edges = sorted(edgeList, key = lambda x : x[2])
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n

        self.paths = [dict() for _ in range(n)]
        self.pa = [[-1]*15 for _ in range(n)]
        self.mw = [[0]*15 for _ in range(n)]
        self.dep = [0] * n

        visited = [0] * n
        for u, v, dis in self.edges:
            pu, pv = self.find(u), self.find(v)
            if pu == pv:
                continue
            self.union(u, v)
            self.paths[u][v] = dis
            self.paths[v][u] = dis


        def dfs(node):
            visited[node] = 1
            for v, dis in self.paths[node].items():
                if visited[v]:
                    continue
                self.dep[v] = self.dep[node] + 1
                self.pa[v][0] = node
                self.mw[v][0] = dis
                dfs(v)

        for i in range(n):
            if visited[i]:
                continue
            self.dep[i] = 1
            dfs(i)
            self.pa[i][0] = i

        for i in range(1, 15):
            for u in range(n):
                self.pa[u][i] = self.pa[self.pa[u][i-1]][i-1]
                self.mw[u][i] = max(self.mw[u][i-1], self.mw[self.pa[u][i-1]][i-1])

    def find(self, x):
        while x != self.parents[x]:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    def union(self, p, q):
        pp, pq = self.find(p), self.find(q)
        if pp == pq:
            return
        if self.sizes[pp] < self.sizes[pq]:
            self.parents[pp] = pq
            self.sizes[pq] += self.sizes[pp]
        else:
            self.parents[pq] = pp
            self.sizes[pp] += self.sizes[pq]

    def query(self, p, q, limit):
        """
        :type p: int
        :type q: int
        :type limit: int
        :rtype: bool
        """
        if self.find(p) != self.find(q):
            return False

        def lca(u, v):
            if self.dep[u] > self.dep[v]:
                u, v = v, u

            diff = self.dep[v] - self.dep[u]
            res = 0
            i = 0
            while diff:
                if diff & 1:
                    res = max(res, self.mw[v][i])
                    v = self.pa[v][i]
                diff >>= 1
                i += 1
            if u == v:
                return res

            for i in range(14, -1, -1):
                if self.pa[v][i] != self.pa[u][i]:
                    res = max(res, self.mw[u][i], self.mw[v][i])
                    v = self.pa[v][i]
                    u = self.pa[u][i]
            res = max(res, self.mw[u][0], self.mw[v][0])
            return res

        return lca(p, q) < limit



# Your DistanceLimitedPathsExist object will be instantiated and called as such:
obj = DistanceLimitedPathsExist(6, [[0, 2, 4], [0, 3, 2], [1, 2, 3], [2, 3, 1], [4, 5, 5]])
res = obj.query(2, 3, 2)
print(res)
res = obj.query(1, 3, 3)
print(res)
res = obj.query(2, 0, 3)
print(res)
res = obj.query(0, 5, 6)
print(res)