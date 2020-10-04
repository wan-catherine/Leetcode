import math


class Solution(object):
    def visiblePoints(self, points, angle, location):
        """
        :type points: List[List[int]]
        :type angle: int
        :type location: List[int]
        :rtype: int
        """
        angles, same = [], 0
        for x, y in points:
            if x == location[0] and y == location[1]:
                same += 1
                continue
            angles.append(math.atan2(y - location[1], x - location[0]))

        angles.sort()
        angles += [x + 2.0 * math.pi for x in angles]

        start, end = 0, 0
        length = len(angles)
        base = angle * math.pi / 180
        res = 0
        while end < length:
            while angles[end] - angles[start] > base:
                start += 1
            res = max(res, end - start + 1)
            end += 1
        return res + same