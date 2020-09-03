class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        self.parents = {}
        self.sizes = {}
        n = len(edges)
        for i in range(1, n+1):
            self.parents[i] = i
            self.sizes[i] = 1

        for u, v in edges:
            u_p, v_p = self.find(u), self.find(v)
            if u_p != v_p:
                self.union(u, v)
            else:
                return [u,v]


    def union(self, a, b):
        a_p = self.find(a)
        b_p = self.find(b)
        if a_p == b_p:
            return
        if self.sizes[a_p] < self.sizes[b_p]:
            self.parents[a_p] = self.parents[b_p]
            self.sizes[b_p] += self.sizes[a_p]
        else:
            self.parents[b_p] = self.parents[a_p]
            self.sizes[a_p] += self.sizes[a_p]

    def find(self, a):
        parent = self.parents[a]
        while self.parents[a] != self.parents[self.parents[a]]:
            self.parents[a] = self.parents[self.parents[a]]
            parent = self.parents[a]
        return parent