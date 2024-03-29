import collections
from typing import List
"""
Actually , it better to use DFS. 
All the values of nums are unique, so each i-index only be visited once . 

"""

class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums_len = len(nums)
        count = 0
        for i in range(nums_len):
            if nums[i] < 0:
                continue
            current_index = i
            temp_count = 0
            while nums[current_index] >= 0:
                temp_count += 1
                next_index = nums[current_index]
                nums[current_index] = -1
                current_index = next_index
            count = max(count, temp_count)
        return count

    def arrayNesting(self, nums: List[int]) -> int:
        length = len(nums)
        parent = [i for i in range(length)]
        size = [1] * length
        def find(p):
            if parent[p] != p:
                parent[p] = find(parent[p])
            return parent[p]
        def union(p, q):
            pp, pq = find(p), find(q)
            if pp == pq:
                return
            if size[pp] < size[pq]:
                parent[pp] = pq
            else:
                parent[pq] = pp
        for n in nums:
            union(n, nums[n])
        for i, p in enumerate(parent):
            parent[i] = find(p)
        return max(collections.Counter(parent).values())