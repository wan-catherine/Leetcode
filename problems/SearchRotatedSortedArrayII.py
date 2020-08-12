class Solution:
    def search_old(self, nums, target):
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

    def search(self, nums, target):
        if not nums:
            return False

        length = len(nums)
        left, right = 0, length - 1
        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return True
            if nums[mid] > nums[right]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else :
                    right = mid - 1
            elif nums[mid] < nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                elif target > nums[right] or target < nums[mid]:
                    right = mid - 1
            else:
                right -= 1

        return True if left >= 0 and left < length and nums[left] == target else False