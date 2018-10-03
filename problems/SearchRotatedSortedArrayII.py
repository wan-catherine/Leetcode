class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if nums == None or len(nums) < 1:
            return False

        i = 0
        j = len(nums) - 1
        while i <= j:
            # if nums[i] < target < nums[j]:
            #     return False
            if target == nums[i]:
                return True
            if target == nums[j]:
                return True
            m = (i + j)//2
            if target == nums[m]:
                return True
            if nums[m] < nums[j]:
                if target < nums[m] or target > nums[j]:
                    j = m - 1
                    continue
                else:
                    i = m + 1
                    continue
            elif nums[m] > nums[i]:
                if  target < nums[m] and target > nums[i]:
                    j = m - 1
                    continue
                else:
                    i = m + 1
                    continue
            else:
                j -= 1

        return False