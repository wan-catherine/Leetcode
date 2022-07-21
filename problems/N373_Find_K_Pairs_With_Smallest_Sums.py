import heapq
from bisect import bisect
from typing import List
from heapq import heappop, heappush
"""
According to the heapq documentation, 
the way to customize the heap order is to have each element on the heap to be a tuple, 
with the first tuple element being one that accepts normal Python comparisons.
"""
class Solution(object):
    def kSmallestPairs_TLE(self, nums1, nums2, k):
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

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        l1, l2 = len(nums1), len(nums2)
        l, r = 0, 0
        res = []
        while l < l1 and r < l2:
            if l + 1 < l1 and r + 1 < l2:
                if nums1[0] + nums2[r + 1] >= nums1[l + 1] + nums2[0]:
                    l += 1
                else:
                    r += 1
            elif l + 1 < l1:
                l += 1
            else:
                r += 1
            if (l + 1) * (r + 1) >= k:
                val = nums1[min(l1 - 1, l)] + nums2[min(l2 - 1, r)]
                ll, rr = l, r
                while ll + 1 < l1:
                    if nums2[0] + nums1[ll + 1] <= val:
                        ll += 1
                    else:
                        break
                while rr + 1 < l2:
                    if nums1[0] + nums2[rr + 1] <= val:
                        rr += 1
                    else:
                        break
                l, r = ll, rr
                break
        for i in range(min(l1, l + 1)):
            for j in range(min(l2, r + 1)):
                res.append([nums1[i], nums2[j]])
        res.sort(key=lambda x: x[0] + x[1])
        return res[:k]

    def kSmallestPairs_GREAT(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heappush(h, [nums1[i] + nums2[j], i, j])

        push(0, 0)
        pairs = []
        while h and len(pairs) < k:
            _, i, j = heappop(h)
            pairs.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:  # 避免重复遍历
                push(i + 1, 0)
        return pairs

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        fl, sl = len(nums1), len(nums2)
        res = []
        if fl * sl <= k:
            for i in range(fl):
                for j in range(sl):
                    res.append([nums1[i], nums2[j]])
            return res

        def check(num):
            ans = 0
            for i in range(fl):
                index = bisect.bisect(nums2, num - nums1[i])
                ans += index
            return ans

        l, r = nums1[0] + nums2[0], nums1[-1] + nums2[-1]
        while l < r:
            mid = (r - l) // 2 + l
            if check(mid) >= k:
                r = mid
            else:
                l = mid + 1
        # print(l)
        for i in range(fl):
            index = bisect.bisect(nums2, l - nums1[i])
            for j in range(index):
                res.append([nums1[i], nums2[j]])
        res.sort(key=lambda x: x[0] + x[1])
        return res[:k]