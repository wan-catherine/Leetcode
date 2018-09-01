class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = nums[0]
        positive = 0
        negative = 0
        flag = False
        for i in nums:
            if i > 0:
                flag = True
                path = positive + negative
                if path <= 0:
                    positive = i
                else:
                    positive = path + i
                if positive > max:
                    max = positive
                negative = 0
            elif flag and i <= 0:
                negative += i
            elif i > max:
                max = i

        return max


