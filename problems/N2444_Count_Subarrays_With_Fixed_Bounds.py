from typing import List


class Solution:
    def countSubarrays_myself(self, nums: List[int], minK: int, maxK: int) -> int:
        intervals = []
        cur = []
        for i, n in enumerate(nums):
            if n > maxK or n < minK:
                if cur:
                    intervals.append(cur)
                    cur = []
            else:
                cur.append(n)
        if cur:
            intervals.append(cur)
        res = 0
        for arr in intervals:
            stack = []
            length = len(arr)
            for i, n in enumerate(arr):
                if n == minK:
                    stack.append((i, -1))
                if n == maxK:
                    stack.append((i, 1))
            cur = 0
            i = 0
            while stack:
                l, v = stack[i]
                r = i + 1
                while r < len(stack):
                    if stack[r][1] + v == 0:
                        break
                    r += 1

                if r == len(stack):
                    break
                res += (l - cur + 1) * (length - stack[r][0])
                cur = l + 1
                i += 1

        return res

    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        length = len(nums)
        res, left = 0, 0
        f, s = -1, -1
        for right in range(length):
            if nums[right] == minK:
                f = right
            if nums[right] == maxK:
                s = right
            if nums[right] < minK or nums[right] > maxK:
                left = right + 1
            res += max(0, min(f, s) - left + 1)
        return res