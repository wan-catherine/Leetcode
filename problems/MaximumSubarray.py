from math import inf


class Solution:
    def maxSubArray_before(self, nums):
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

    def maxSubArray_kadane(self, nums):
        if not nums:
            return None
        previous = nums[0]
        res = previous
        for i in nums[1:]:
            if previous > 0:
                previous = previous + i
            else:
                previous = i
            res = max(res, previous)
        return res

    # ok, now I understand Kadane's algorithm
    def maxSubArray(self, nums):
        if not nums:
            return None
        res = float(-inf)
        previous = res
        for i in nums:
            if previous > 0:
                previous += i
            else:
                previous = i
            res = max(previous, res)
        return res


