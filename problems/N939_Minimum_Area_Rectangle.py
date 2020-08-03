import collections


class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        x_map = collections.defaultdict(set)
        for li in points:
            x_map[li[0]].add(li[1])

        length = len(x_map)
        res = 40001 ** 2
        keys = list(x_map.keys())
        for i in range(length):
            for j in range(i+1, length):
                overlap = x_map[keys[i]].intersection(x_map[keys[j]])
                if not overlap or len(overlap) < 2:
                    continue
                y = 40001
                overlap_li = sorted(overlap)
                for k in range(1, len(overlap_li)):
                    y = min(y, overlap_li[k] - overlap_li[k-1])
                res = min(res, abs((keys[i]-keys[j])*y))
        return res if res != 40001 ** 2 else 0


