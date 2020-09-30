import heapq
"""
According to the heapq documentation, 
the way to customize the heap order is to have each element on the heap to be a tuple, 
with the first tuple element being one that accepts normal Python comparisons.
"""
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0 or not nums1 or not nums2:
            return []
        heap = []
        for i in nums1:
            for j in nums2:
                heapq.heappush(heap, (i+j, i, j))
        ans = heapq.nsmallest(k, heap)
        res = []
        for _, i, j in ans:
            res.append([i, j])
        return res
