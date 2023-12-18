from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        def check(n):
            sn = str(n)
            return sn == sn[::-1]

        def helper(a):
            res = 0
            for n in nums:
                res += abs(a - n)
            return res

        length = len(nums)
        nums.sort()
        if length % 2 == 1:
            mid = nums[length//2]
        else:
            mid = (nums[length//2 - 1] + nums[length//2]) // 2
        if check(mid):
            return helper(mid)

        less, more = mid - 1, mid + 1
        while less > 0:
            if check(less):
                break
            less -= 1
        while True:
            if check(more):
                break
            more += 1
        return min(helper(less), helper(more))

