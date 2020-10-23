"""
Radix Sort:
    1. find the maximum num
    2. calculate the number of maximum num's digit (base on 10) ==> loop times
    3. start from the right most digit to do loop:
    4. each loop , put the related digit into the correct buckets
    5. then get new array from buckets, then do it again.

Notice :
    We need empty bucket for each loop
"""
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 2:
            return 0
        maximum = max(nums)
        times = 1
        while maximum // 10:
            times += 1
            maximum //= 10
        for i in range(times):
            buckets = [[] for _ in range(10)]
            for n in nums:
                index = (n // (10 ** i)) % 10
                buckets[index].append(n)
            nums = []
            for j in buckets:
                nums.extend(j)
        return max([j-i for i, j in zip(nums, nums[1:])])
