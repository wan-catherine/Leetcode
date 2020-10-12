class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        parent = [0]*26
        size = [1]*26
        for i in range(26):
            parent[i] = i

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            pi, pj = find(i), find(j)
            if size[pi] < size[pj]:
                parent[pi] = pj
                size[pj] += size[pi]
            else:
                parent[pj] = pi
                size[pi] += size[pj]

        for s in equations:
            x, op, y = ord(s[0]) - ord('a'), s[1:3], ord(s[3]) - ord('a')
            if op == '!=':
                continue
            union(x, y)

        for s in equations:
            x, op, y = ord(s[0]) - ord('a'), s[1:3], ord(s[3]) - ord('a')
            if op == '==':
                continue
            if find(x) == find(y):
                return False
        return True

