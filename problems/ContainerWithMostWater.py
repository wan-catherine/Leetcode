import math
class Solution:
    def maxArea_slowversion(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = [0] * len(height)
        for i in range(1, len(height)):
            res[i] = res[i - 1]
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

    def maxArea_largeSpace(self, height):
        length = len(height)
        highest = max(height) + 1
        if highest < length:
            highest = length

        area = [[0 for x in range(highest)] for y in range(highest)]

        res = [0] * length
        for i in range(1, length):
            res[i] = res[i - 1]
            for x in range(0, i):
                if height[x] >= height[i]:
                    if area[i - x][height[i]] == 0:
                        s = (i - x) * height[i]
                        area[i - x][height[i]] = s
                        area[height[i]][i - x] = s
                    else:
                        s = area[i - x][height[i]]
                    if s > res[i]:
                        res[i] = s
                    break
                elif height[x] < height[i]:
                    if area[i - x][height[i]] == 0:
                        s = (i - x) * height[x]
                        area[i - x][height[x]] = s
                        area[height[x]][i - x] = s
                    else:
                        s = area[i - x][height[i]]
                    if s > res[i]:
                        res[i] =s
        return  res[len(height) - 1]

    def maxArea(self, height):
        length = len(height)
        if length < 2:
            return 0

        i = 0
        j = length - 1
        res = 0
        while i < j:
            if height[i] <= height[j]:
                area = (j - i) * height[i]
                i += 1
            else:
                area = (j - i) * height[j]
                j -= 1
            if area > res:
                res = area
        return  res



