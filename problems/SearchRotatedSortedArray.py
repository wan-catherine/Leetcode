class Solution:
    def search_old(self, nums, target):
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

    def search_(self, nums, target):
        if not nums:
            return -1

        length = len(nums)
        left, right = 0, length - 1
        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[right]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                elif target > nums[right] or target < nums[mid]:
                    right = mid - 1
        return left if left >= 0 and left < length and nums[left] == target else -1
    """
    1. check whether nums[mid] and target in the same sorted array.
    2. if they are in the same (left or right), ten it's a normal binary search 
    3. if they are in the different sorted array, then :
        a. if mid in the left, move to right : left = mid + 1
        b. if mid in the right, move to left : right = mid - 1
    """
    def search(self, nums, target: int) -> int:
        length = len(nums)
        left, right = 0, length - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return mid

            if (nums[mid] >= nums[0]) == (target >= nums[0]):
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid - 1
        return -1