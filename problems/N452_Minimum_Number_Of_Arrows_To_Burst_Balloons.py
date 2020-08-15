class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        points.sort(key=lambda li: li[0])
        current = points[0]
        res = 1
        length = len(points)

        for i in range(1, length):
            if points[i][0] > current[1]:
                res += 1
                current = points[i]
            else:
                current[1] = min(current[1], points[i][1])
        return res

