class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums_len = len(nums)
        count = 0
        for i in range(nums_len):
            if nums[i] < 0:
                continue
            current_index = i
            temp_count = 0
            while nums[current_index] >= 0:
                temp_count += 1
                next_index = nums[current_index]
                nums[current_index] = -1
                current_index = next_index
            count = max(count, temp_count)
        return count

