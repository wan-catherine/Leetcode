class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sortedNums = sorted(nums)
        i = 0
        j = len(nums) - 1
        while i < j:
            if sortedNums[i] + sortedNums[j] < target:
                i += 1
            elif sortedNums[i] + sortedNums[j] > target:
                j -= 1
            else:
                break
        index_i = nums.index(sortedNums[i])
        if sortedNums[i] != sortedNums[j]:
            index_j = nums.index(sortedNums[j])
        else:
            index_j = nums.index(sortedNums[j], index_i + 1)

        if index_i < index_j:
            return [index_i, index_j]
        else:
            return [index_j, index_i]
