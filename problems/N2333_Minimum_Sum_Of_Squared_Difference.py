from typing import List


class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        length, k = len(nums1), k1 + k2
        status = [0] * (10 ** 5 + 1)
        total = 0
        for i in range(length):
            diff = abs(nums1[i] - nums2[i])
            total += diff
            status[diff] += 1
        if k >= total:
            return 0
        for i in range(10 ** 5, -1, -1):
            if status[i] == 0:
                continue
            if k >= status[i]:
                k -= status[i]
                status[i-1] += status[i]
                status[i] = 0
            else:
                status[i] -= k
                status[i-1] += k
                k = 0
            if k == 0:
                break
        res = 0
        for i in range(1, 10**5 + 1):
            if status[i] == 0:
                continue
            res += i * i * status[i]
        return res


