class Solution(object):
    def nextPermutation_before(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        max = nums[len(nums) - 1]
        k = -1
        for index in range(len(nums) -2, -1, -1):
            if nums[index] >= max:
                max = nums[index]
                continue

            k = index + 1
            i = len(nums) - 1
            while k < len(nums):
                if nums[index] < nums[k]:
                    k += 1
                else:
                    i = k - 1
                    break
            nums[index], nums[i] = nums[i], nums[index]
            nums[index + 1:] = sorted(nums[index + 1:])
            break
        if k == -1:
            nums.reverse()
        return nums
    """
    find the rules of how to create permutation
    a. Find the descrease part of the array which means it uses up all possibility
    b. Change the next number of this descrease arary with the number > itself.
    c. reverse all the left numbers in the array
    
    The key point here is to deal with the corner condition
    """
    def nextPermutation(self, nums):
        length = len(nums)
        i = length - 1
        while i > 0:
            if nums[i] <= nums[i-1]:
                i -= 1
            else:
                break
        if i < length - 1:
            if i > 0:
                for j in range(length-1,-1,-1):
                    if nums[i-1] < nums[j]:
                        nums[i-1],nums[j] = nums[j],nums[i-1]
                        break

            left, right = i, length - 1
            while left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        else:
            nums[i],nums[i-1] = nums[i-1], nums[i]
        return nums


