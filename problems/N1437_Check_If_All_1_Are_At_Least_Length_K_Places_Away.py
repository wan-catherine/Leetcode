class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        count = 0 if nums[0] == 0 else k
        for i in nums:
            if i == 1:
                if count < k:
                    return False
                else:
                    count = 0
            else:
                count += 1
        return True

