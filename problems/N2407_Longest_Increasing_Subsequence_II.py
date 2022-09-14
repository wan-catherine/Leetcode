from typing import List
from Template.Segment_Tree import SegTreePoint, SegTreeArray

class Solution:
    def lengthOfLIS_TLE(self, nums: List[int], k: int) -> int:
        val = max(nums)
        root = SegTreePoint(0, val, 0)
        root.buildTree(0, val, 0)
        res = 0
        prev = -1
        for num in nums:
            if num == prev:
                continue
            prev = num
            l = root.queryRange(max(0, num - k), max(0, num - 1))
            root.updateRange(num, num, l+1)
            res = max(res, l+1)
        return res

    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        val = max(nums)
        ans = 0
        root = SegTreeArray(val)
        for num in nums:
            num -= 1
            l = root.query(max(0, num-k), num)
            ans = max(ans, l + 1)
            root.update(num, l + 1)
        return ans

    def lengthOfLIS_ok(self, nums: List[int], k: int) -> int:
        val = max(nums)
        ans = 0
        root = SegTreeArray(val + 1)
        for num in nums:
            l = root.query(max(0, num-k), num)
            ans = max(ans, l + 1)
            root.update(num, l + 1)
        return ans