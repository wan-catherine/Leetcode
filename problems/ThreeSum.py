import collections
from typing import List


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 3:
            return []

        nums = sorted(nums)
        res = []
        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break

            base = 0 - nums[i]
            p = i + 1
            q = length - 1
            while p < q:
                if nums[p] + nums[q] < base:
                    p += 1
                elif nums[p] + nums[q] > base:
                    q -= 1
                else:
                    while p + 1 < length and nums[p] == nums[p + 1]:
                        p += 1
                    while q > 0 and nums[q] == nums[q - 1]:
                        q -= 1
                    res.append([nums[i], nums[p], nums[q]])
                    p += 1
                    q -= 1
        return res

    def threeSum_hashtable(self, nums: List[int]) -> List[List[int]]:
        counter = collections.defaultdict(list)
        length = len(nums)
        nums.sort()
        for i in range(length):
            counter[nums[i]].append(i)
        res = []
        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            two = -nums[i]
            for j in range(i+1, length):
                if j-1 != i and nums[j] == nums[j-1]:
                    continue
                val = nums[j]
                target = two - val
                if target not in counter or counter[target][-1] <= j:
                    continue
                res.append([nums[i], nums[j], target])
        return res

