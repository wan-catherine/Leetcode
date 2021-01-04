import bisect


class Solution(object):
    def minOperations(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: int
        """
        length = len(target)
        mapping = {target[i]:i for i in range(length)}
        nums = []
        for num in arr:
            if num not in mapping:
                continue
            nums.append(mapping[num])
        array = []
        for i, n in enumerate(nums):
            index = bisect.bisect_left(array, n)
            if index == len(array):
                array.append(n)
            else:
                array[index] = n
        return length - len(array)

