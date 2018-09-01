class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 1:
            return  -1

        i = 0
        j = len(nums) - 1
        point = -1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] >= nums[i]:
                if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                    point = mid
                    break
                else:
                    i = mid + 1
            elif nums[mid] < nums[j]:
                if mid > 0 and nums[mid] < nums[mid - 1]:
                    point = mid - 1
                    break
                else:
                    j = mid - 1

        if target < nums[point + 1] or target > nums[point] or nums[len(nums) -1] < target < nums[0]:
            return -1
        elif nums[point + 1] <= target <= nums[len(nums) - 1]:
            i = point + 1
            j = len(nums) - 1
        else:
            i = 0
            j = point

        index = -1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                index = mid
                break
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1

        return index
