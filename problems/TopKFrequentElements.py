class Solution:
    def topKFrequent_before(self, nums, k):
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

    def topKFrequent(self, nums, k):
        n_count_mapping = {}
        for i in nums:
            n_count_mapping[i] = n_count_mapping.setdefault(i, 0) + 1

        keys = sorted(n_count_mapping, key=n_count_mapping.get, reverse=True)
        return keys[:k]


