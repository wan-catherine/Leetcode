from math import inf


class Solution:
    def trap_before(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<3:
            return 0
        left = [0] * len(height)
        right = [0] * len(height)

        left[0] = height[0]
        for i in range(1,len(height)):
            left[i] = height[i] if height[i] > left[i - 1] else left[i - 1]

        right[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            right[i] = height[i] if height[i] > right[i + 1] else right[i + 1]

        res = 0
        for i in range(0, len(height)):
            res += min(left[i], right[i]) - height[i]

        return res


    def trap(self, height):
        height = [float(inf)] + height + [float(inf)]
        stack = []
        res = 0
        for index, value in enumerate(height):
            #non-increasing stack
            while stack and height[stack[-1]] < value:
                cur = stack.pop()
                previous = stack[-1]
                if height[previous] != float(inf) and height[index] != float(inf):
                    res += (min(height[index], height[previous]) - height[cur]) * (index - previous - 1)
            stack.append(index)
        return res

