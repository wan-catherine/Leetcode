import math
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = [0] * len(height)
        for i in range(1, len(height)):
            res[i] = res[i - 1]
            x = 0
            h = 0
            for x in range(0, i):
                if height[x] >= height[i]:
                    s = (i - x) * height[i]
                    if s > res[i]:
                        res[i] = s
                    break
                elif height[x] < height[i]:
                    s = (i - x) * height[x]
                    if s > res[i]:
                        res[i] =s

        return res[len(height) - 1]