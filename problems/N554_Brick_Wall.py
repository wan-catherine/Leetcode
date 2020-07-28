import collections


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        count = collections.defaultdict(int)
        for li in wall:
            length = len(li)
            if length < 2:
                continue
            temp = li[0]
            count[li[0]] += 1
            for i in range(1, length - 1):
                temp += li[i]
                count[temp] += 1

        rows = len(wall)
        res = 0
        for i in count:
            res = max(res, count[i])
        return rows - res
