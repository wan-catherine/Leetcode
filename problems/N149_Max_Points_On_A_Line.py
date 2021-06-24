import collections
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        mapping = collections.defaultdict(set)
        length = len(points)
        for i in range(length):
            x1, y1 = points[i]
            for j in range(i+1, length):
                x2, y2 = points[j]
                if x1 == x2:
                    mapping['#' + str(x1)].add(i)
                    mapping['#' + str(x1)].add(j)
                elif y1 == y2:
                    mapping['0' + str(y1)].add(i)
                    mapping['0' + str(y1)].add(j)
                else:
                    k = (y2 - y1)/(x2 - x1)
                    y = y2 - k*x2
                    key = "{0}|{1}".format(y, k)
                    mapping[key].add(i)
                    mapping[key].add(j)
        res = 1
        for key in mapping:
            res = max(res, len(mapping[key]))
        return res