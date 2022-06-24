from typing import List


class Solution(object):
    def maxSumOfThreeSubarrays_oneway(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        first_sum, second_sum, third_sum = sum(nums[:k]), sum(nums[k:2*k]), sum(nums[2*k:3*k])
        one_total_sum, two_total_sum , three_total_sum = first_sum, first_sum + second_sum, first_sum + second_sum + third_sum
        one, two, three = [0], [0, k], [0, k, 2*k]
        length = len(nums)
        for i in range(1, length-3*k+1):
            first_sum = first_sum - nums[i-1] + nums[i+k-1]
            if first_sum > one_total_sum:
                one = [i]
                one_total_sum = first_sum
            second_sum = second_sum - nums[i+k-1] + nums[i+2*k-1]
            if second_sum + one_total_sum > two_total_sum:
                two_total_sum = second_sum + one_total_sum
                two = one + [i+k]
            third_sum = third_sum - nums[i+2*k-1] + nums[i+3*k-1]
            if third_sum + two_total_sum > three_total_sum:
                three_total_sum = third_sum + two_total_sum
                three = two + [i+2*k]
        return three

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        left, right, middle = [None] * length, [None] * length, [0] * length
        cur = sum(nums[:k])
        middle[0] = cur
        for i in range(1, length - k + 1):
            cur = cur - nums[i-1] + nums[i+k-1]
            middle[i] = cur
        cur = sum(nums[:k])
        li = 0
        for i in range(k, length - k):
            if middle[i - k] > cur:
                cur = middle[i-k]
                li = i-k
            left[i] = (cur, li)
        cur = middle[length - k]
        ri = length - k
        for i in range(length - 2 * k, k-1, -1):
            if middle[i+k] >= cur:
                cur = middle[i+k]
                ri = i + k
            right[i] = (cur, ri)

        res = 0
        ans = [-1, -1, -1]
        for i in range(k, length - 2*k + 1):
            val = left[i][0] + middle[i] + right[i][0]
            if val > res:
                res = val
                ans = [left[i][1], i, right[i][1]]
        return ans
