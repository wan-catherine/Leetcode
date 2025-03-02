from typing import List


class Solution:
    """
    count is a 32bit integer which is a counter and each bit can only be 0 or 1
    while count & nums[i] == 0, count + nums[i] means set the bit to 1
    for example , 3 and 8
     011
    +100
    =111
    """

    def longestNiceSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        count = 0
        res = 0
        j = 0
        for i in range(length):
            while j < length and count & nums[j] == 0:
                count += nums[j]
                j += 1
            res = max(res, j - i)
            count -= nums[i]
        return res

    def longestNiceSubarray_me(self, nums: List[int]) -> int:
        length = len(nums)
        arr = [0] * 32
        left = 0
        res = 1
        def check():
            for i in arr:
                if i > 1:
                    return True
            return False
        for right in range(length):
            v = nums[right]
            i = 0
            while v > 0:
                if v % 2 == 1:
                    arr[i] += 1
                v //= 2
                i += 1
            while check():
                val = nums[left]
                j = 0
                while val > 0:
                    if val % 2 == 1:
                        arr[j] -= 1
                    val //= 2
                    j += 1
                left += 1
            res = max(res, right - left + 1)
        return res

