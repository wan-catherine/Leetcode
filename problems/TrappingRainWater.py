class Solution:
    def trap(self, height):
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

