class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
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



