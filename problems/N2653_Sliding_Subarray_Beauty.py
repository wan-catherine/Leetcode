from typing import List


class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        arr = [0] * 51
        for i in range(k-1):
            if nums[i] < 0:
                arr[-nums[i]] += 1
        length = len(nums)
        res = []
        for i in range(k-1, length):
            if nums[i] < 0:
                arr[-nums[i]] += 1

            count = 0
            ans = 0
            for j in range(50, 0, -1):
                if arr[j] >= 1:
                    count += arr[j]
                    if count >= x:
                        ans = -j
                        break
            res.append(ans)
            if nums[i-k+1] < 0:
                arr[-nums[i-k+1]] -= 1
        return res
