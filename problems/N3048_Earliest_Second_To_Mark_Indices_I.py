from typing import List


class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        nums = [0] + nums
        changeIndices = [0] + changeIndices
        n, m = len(nums), len(changeIndices)
        def check(t):
            last = [0] * n
            for i in range(t+1):
                last[changeIndices[i]] = i
            for i in range(1, n):
                if last[i] == 0:
                    return False
            count = 0
            for i in range(1, t+1):
                if i == last[changeIndices[i]]:
                    val = count - nums[changeIndices[i]]
                    if val >= 0:
                        count = val
                    else:
                        return False
                else:
                    count += 1
            return True

        l, r = 0, m
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1

        return l if l > 0 and l < m else -1