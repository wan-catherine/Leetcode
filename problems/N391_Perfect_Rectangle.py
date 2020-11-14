import collections
"""
1. sum of the area of all small rectangles equals to the final large rectangle's area
2. all lbnodes and runodes should not be duplicated 
3. the four nodes for the final rectangle should only show one time
"""

class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        leftb,leftu, rightb, rightu = [], [], [], []

        area = 0
        nodes = []
        lbnodes, runodes = [], []
        for i, j, p, q in rectangles:
            leftb.append((i, j))
            rightu.append((p, q))
            area += (p - i) * (q - j)
            nodes.extend([(i, j), (p, q), (i, q), (p, j)])
            lbnodes.append((i, j))
            runodes.append((p, q))

        l_b = min(leftb)
        r_u = max(rightu)
        l_u = (l_b[0], r_u[1])
        r_b = (r_u[0], l_b[1])

        if len(lbnodes) != len(set(lbnodes)) or len(runodes) != len(set(runodes)):
            return False

        new_area = (r_u[0] - l_b[0]) * (r_u[1] - l_b[1])
        if new_area != area:
            return False

        counter = collections.Counter(nodes)
        if counter[l_b] != 1 or counter[l_u] != 1 or counter[r_b] != 1 or counter[r_u] != 1:
            return False

        for key, value in counter.items():
            if value == 1 and key not in [l_b, r_u, l_u, r_b]:
                return False
        return True


