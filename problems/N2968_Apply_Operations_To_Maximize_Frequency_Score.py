from typing import List


class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums = [0] + nums
        length = len(nums)
        nums.sort()
        pre = [0] * length
        for i in range(1, length):
            pre[i] = pre[i-1] + nums[i]

        def check(l, r):
            mid = (r + l) // 2
            cout = nums[mid] * (mid - l + 1) - (pre[mid] - pre[l-1])
            cout += pre[r] - pre[mid] - nums[mid] * (r - mid)
            return cout <= k

        res = 0
        r = 1
        for l in range(1, length):
            while r < length and check(l, r):
                res = max(res, r - l + 1)
                r += 1
        return res
