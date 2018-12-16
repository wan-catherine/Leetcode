class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        length = len(nums)
        if nums == None or length < 1 :
            return False
        if len(set(nums)) == length and t == 0:
            return False

        res = False
        for i in range(length):
            if i + k >= length:
                res = self.check(nums[i:], t)
            else:
                res = self.check(nums[i:i+k+1], t)
            if res:
                return res

        return res


    def check(self, nums, t):
        if len(nums) < 2:
            return False
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] <= t:
                return True
        return False

