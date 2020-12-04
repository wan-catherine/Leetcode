import bisect


class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        def count(val):
            length = len(nums)
            count = 0
            for i in range(length):
                v = nums[i] + val
                index = bisect.bisect(nums, v)
                count += index - i - (1 if index == length or nums[i] != v else 0)
            return count

        left, right = 0, nums[-1] + 1
        while left < right:
            mid = (right - left) // 2 + left
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left 

