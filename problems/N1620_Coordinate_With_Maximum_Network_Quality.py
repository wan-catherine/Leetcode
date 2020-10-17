import collections
import math


class Solution(object):
    def bestCoordinate(self, towers, radius):
        """
        :type towers: List[List[int]]
        :type radius: int
        :rtype: List[int]
        """
        large = 0
        res = []
        mapping = collections.defaultdict(int)
        for x, y, q in towers:
            for i in range(-radius, radius+1):
                for j in range(-radius, radius+1):
                    x1, y1 = x+i, y+j
                    dist = math.sqrt(i**2 + j**2)
                    if dist > radius:
                        continue
                    quality = math.floor(q / (1 + dist))
                    mapping[(x1,y1)] += quality
                    if mapping[(x1,y1)] > large:
                        large = mapping[(x1, y1)]
                        res = [(x1, y1)]
                    elif mapping[(x1, y1)] == large:
                        res.append((x1, y1))

        res.sort()
        return list(res[0])