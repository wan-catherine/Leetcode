class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if nums == None or len(nums) < 1 or len(nums) == len(set(nums)):
            return False

        mapping = {}
        for i in range(len(nums)):
            if nums[i] not in mapping:
                mapping[nums[i]] = [i]
            else:
                if i - mapping[nums[i]][-1] <= k:
                    return True
                mapping[nums[i]].append(i)

        return False