"""
Union-Find
get component needs to use group(find)
"""
class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        alice, bob, common = set(), set(), set()
        for type, u, v in edges:
            if type == 1:
                alice.add((u,v))
            elif type == 2:
                bob.add((u,v))
            else:
                common.add((u,v))

        parents = [i for i in range(n+1)]
        size = [1 for i in range(n+1)]

        res = 0
        for u, v in common:
            if not self.union(u, v, parents, size):
                res += 1

        group = set()
        for i in range(1, n+1):
            group.add(self.find(i, parents))
        if len(group) == 1:
            return res + len(alice) + len(bob)

        # Alice
        a_parents = parents[:]
        a_size = size[:]
        for u, v in alice:
            if not self.union(u, v, a_parents, a_size):
                res += 1
        group = set()
        for i in range(1, n+1):
            group.add(self.find(i, a_parents))
        if len(group) != 1:
            return -1

        # Bob
        b_parents = parents[:]
        b_size = size[:]
        for u, v in bob:
            if not self.union(u, v, b_parents, b_size):
                res += 1
        group = set()
        for i in range(1, n+1):
            group.add(self.find(i, b_parents))
        if len(group) != 1:
            return -1
        return res

    def union(self, a, b, parents, size):
        a_p, b_p = self.find(a, parents), self.find(b, parents)
        if a_p == b_p:
            return False
        if size[a_p] < size[b_p]:
            parents[a_p] = b_p
            size[b_p] += size[a_p]
        else:
            parents[b_p] = a_p
            size[a_p] += size[b_p]
        return True

    def find(self, a, parents):
        while parents[a] != a:
            parents[a] = parents[parents[a]]
            a = parents[a]
        return a
