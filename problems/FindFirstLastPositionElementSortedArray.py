class Solution:
    def searchRange_slow(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        if length < 1:
            return [-1, -1]

        i = 0
        j = length - 1
        while i <= j:
            if nums[i] == target and nums[j] == target:
                break
            middle = (j + i) // 2
            if nums[middle] < target:
                i = middle + 1
            elif nums[middle] > target:
                j = middle - 1
            else:
                left = middle - 1
                if nums[left] == target:
                    while i <= left and nums[i] != target:
                        mleft = (i + left) // 2
                        if nums[mleft] < target:
                            i = mleft + 1
                        else:
                            left = mleft
                else:
                    i = middle
                right = middle + 1
                if nums[right] == target:
                    while j >= right and nums[j] != target:
                        mright = (j + right) // 2
                        if nums[mright] > target:
                            j = mright - 1
                        else:
                            right = mright
                else:
                    j = middle

        if i > j:
            return [-1, -1]
        return [i, j]

    def searchRange(self, nums, target):
        i = 0
        j = len(nums) - 1
        if j < i:
            return [-1, -1]
        while i < j:
            middle = (i + j) // 2
            if nums[middle] < target:
                i = middle + 1
            else:
                j = middle
        if nums[i] != target:
            return [-1, -1]
        else:
            left = i

        j = len(nums) - 1
        while i < j:
            middle = (i + j)//2 + 1
            if nums[middle] > target:
                j = middle - 1
            else:
                i = middle
        return [left, j]