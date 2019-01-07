class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from heapq import nlargest
        if len(nums) == k:
            return nums

        res = {}
        for i in nums:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1

        l = list(res.items())
        return [val[0] for val in nlargest(k, l, key= lambda e:e[1])]