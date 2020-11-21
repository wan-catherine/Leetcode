import bisect


class Solution(object):
    def atMostNGivenDigitSet(self, digits, n):
        """
        :type digits: List[str]
        :type n: int
        :rtype: int
        """
        digits = [int(i) for i in digits]
        digits.sort()
        nums = []
        while n:
            nums.append(n%10)
            n //= 10

        length = len(nums)
        res = 0
        d_count = len(digits)

        if length > 1:
            if d_count > 1:
                res = d_count * (1 - d_count ** (length - 1)) // (1 - d_count)
            else:
                res = length - 1

        def helper(arr):
            nonlocal res, d_count
            if not arr:
                return
            index = bisect.bisect_left(digits, arr[-1])
            if index == len(digits) or digits[index] != arr[-1]:
                res += index * (d_count ** (len(arr) - 1))
            else:
                if len(arr) > 1:
                    res += index  * (d_count ** (len(arr) - 1))
                else:
                    res += index + 1
                helper(arr[:-1])
        helper(nums)
        return res