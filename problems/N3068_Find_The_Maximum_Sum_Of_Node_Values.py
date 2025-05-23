from typing import List


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        length = len(nums)
        arr = []
        for n in nums:
            arr.append((n ^ k) - n)
        arr.sort(reverse=True)

        diff = 0

        for i in range(length):
            if arr[i] > 0:
                diff += arr[i]
            elif arr[i] == 0:
                break
            else:
                if i % 2 == 0:
                    break
                else:
                    diff = max(diff + arr[i], diff - arr[i-1])
                    break
        if arr[-1] > 0:
            if length % 2 == 1:
                diff -= arr[-1]

        return diff + sum(nums)

    def maximumValueSum_20250523(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        length = len(nums)
        arr = []
        for n in nums:
            arr.append((n ^ k) - n)
        arr.sort(reverse=True)

        md, cd = 0, 0
        for i in range(0, length, 2):
            cd += arr[i]
            if i + 1 == length:
                break
            cd += arr[i + 1]
            if cd > md:
                md = cd

        return md + sum(nums)




