import collections

"""
find the friends' cycle. 
the couple belongs to the same friends' cycle.
the row[i], row[i+1] also belongs to the same friends' cycle. 
do union, to find how many friends' cycle. 
For each cycle, the sway == n//2 -1 (n is the number of people in the cycle).
"""
class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        length = len(row)
        parents = [0] * length
        for i in range(0, length, 2):
            parents[i] = i
            parents[i+1] = i

        def find(x):
            while x != parents[x]:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x

        def union(p, q):
            parents[p] = q

        for i in range(0, length, 2):
            pp, pq = find(row[i]), find(row[i+1])
            if pp == pq:
                continue
            union(pp, pq)

        res = 0
        mapping = collections.defaultdict(int)
        for p in parents:
            pp = find(p)
            mapping[pp] += 1

        for key, value in mapping.items():
            res += value//2 - 1

        return res
