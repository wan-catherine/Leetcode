from typing import List


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        minsum = float("inf")
        for i in range(len(nums) - 2):
            p = i + 1
            q = len(nums) - 1
            lesssum = float("inf") * (-1)
            moresum = float("inf")
            while p < q:
                sum = nums[i] + nums[p] + nums[q]
                if sum == target:
                    return target
                elif sum < target:
                    if sum > lesssum:
                        lesssum = sum
                    p += 1
                elif sum > target:
                    if sum < moresum:
                        moresum = sum
                    q -= 1
            if abs(minsum - target) > abs(lesssum - target) and abs(lesssum - target) < abs(moresum - target) :
                minsum = lesssum
            elif abs(minsum - target) > abs(moresum - target) and abs(moresum - target) < abs(lesssum - target):
                minsum = moresum
        return minsum

    def threeSumClosest_20250111(self, nums: List[int], target: int) -> int:
        length = len(nums)
        res = sys.maxsize
        nums.sort()
        pi = -1001
        for i in range(length):
            if pi == nums[i]:
                continue
            pi = nums[i]
            l, r = i + 1, length - 1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if val == target:
                    return target
                if val > target:
                    r -= 1
                else:
                    l += 1
                if abs(val - target) < abs(res - target):
                    res = val
        return res





        