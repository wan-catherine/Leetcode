import bisect


class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        previous = 0
        horizontalCuts.sort()
        max_h = 0
        for l in horizontalCuts:
            max_h = max(max_h, l - previous)
            previous = l
        max_h = max(max_h, h - horizontalCuts[-1])

        previous = 0
        verticalCuts.sort()
        max_v = 0
        for v in verticalCuts:
            max_v = max(max_v, v - previous)
            previous = v
        max_v = max(max_v, w - verticalCuts[-1])

        return max_v * max_h % (10**9 + 7)
