import collections
from typing import List


class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        length = len(nums)
        def atMost(k):
            if k == 0:
                return 0
            res, j = 0, 0
            status = collections.defaultdict(int)
            for i in range(length):
                while j < length and (nums[j] in status or len(status) < k):
                    status[nums[j]] += 1
                    j += 1
                res += j - i
                if status[nums[i]] == 1:
                    del status[nums[i]]
                else:
                    status[nums[i]] -= 1
            return res


        total = length * (length + 1) // 2
        point = (total + 1) // 2
        l, r = 0, length
        while l < r:
            mid = l + (r - l) // 2
            if atMost(mid) >= point:
                r = mid
            else:
                l = mid + 1
        return l