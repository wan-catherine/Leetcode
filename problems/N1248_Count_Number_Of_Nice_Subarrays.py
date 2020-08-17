class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        index = []
        for i in range(len(nums)):
            if nums[i] % 2:
                index.append(i)

        length = len(index)
        if length < k:
            return 0

        start, end = 0,0
        res = 0
        while end < length:
            k -= 1
            if k == 0:
                if start == 0:
                    left = index[start] + 1
                else:
                    left = index[start] - index[start - 1]
                if end == length - 1 :
                    right = len(nums) - index[end]
                else:
                    right = index[end + 1] - index[end]
                res += left * right
                start += 1
                k += 1
            end += 1
        return res