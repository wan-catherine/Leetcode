import collections


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

    def topKFrequent_sort(self, nums, k):
        n_count_mapping = {}
        for i in nums:
            n_count_mapping[i] = n_count_mapping.setdefault(i, 0) + 1

        keys = sorted(n_count_mapping, key=n_count_mapping.get, reverse=True)
        return keys[:k]

    """
    20200620 update
    Use bucket sort
    need to get the max_frequent 
    buckets:
        key : frequent
        value : nums which have same frequency 
    Time complexity : O(n)
    """
    def topKFrequent(self, nums, k):
        num_count_mapping = collections.defaultdict(int)
        for num in nums:
            num_count_mapping[num] += 1
        buckets = collections.defaultdict(list)
        max_frequent = 0
        for key, value in num_count_mapping.items():
            buckets[value].append(key)
            max_frequent = max(max_frequent, value)

        res = []
        while max_frequent > 0:
            if buckets[max_frequent] == 0:
                max_frequent -= 1
                continue
            length = len(buckets[max_frequent])
            if k >= length:
                res.extend(buckets[max_frequent])
                k -= length
                max_frequent -= 1
            if k == 0:
                break
        return res




