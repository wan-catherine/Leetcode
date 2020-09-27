import collections
"""
I failed 10 times!!!
key points:
    1. sums up to n*k where n is also an integer. so n can be zero which means any two num in nums equal to zero, then it will be True.
    2. If k == 0, and there is no two num in nums equal to zero, then it will be False.
    3. if remainder (i > 0) equal to zero, it means at least there are two num in nums which sum is k, so it will be True. 
    4. if remainder != 0, then we need to check if there are two prefixes have same remainder . At this time, need to make sure the last 
        prefix should >= k . Because two nums can have same remainder but both less than k . 
"""

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        length = len(nums)
        for i in range(1, length):
            if nums[i] == 0 and nums[i-1] == 0:
                return True
        if k == 0:
            return False
        prefix = nums[:]
        mapping = collections.defaultdict(list)
        mapping[nums[0]%k].append(0)
        for i in range(1, length):
            prefix[i] += prefix[i-1]
            remainder = prefix[i]%k
            if remainder == 0:
                return True
            mapping[remainder].append(i)
            if len(mapping[remainder]) >= 2:
                if remainder != 0 and prefix[mapping[remainder][-1]] >= k and mapping[remainder][-1] - mapping[remainder][0] >= 2:
                    return True
        return False
