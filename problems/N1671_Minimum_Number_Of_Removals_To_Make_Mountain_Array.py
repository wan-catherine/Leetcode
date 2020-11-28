import bisect


class Solution(object):
    """
    Find LIS(longest increasing sequence) from start and end.
    Then check the largest mountain array.
    """
    def minimumMountainRemovals_(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        prefix, suffix = [0] * length, [0] * length
        for i in range(1, length):
            for j in range(i):
                if nums[j] < nums[i]:
                    prefix[i] = max(prefix[i], prefix[j] + 1)
        for i in range(length-2, -1, -1):
            for j in range(length-1, i, -1):
                if nums[j] < nums[i]:
                    suffix[i] = max(suffix[i], suffix[j] + 1)
        s = 3
        for i in range(1, length-1):
            s = max(s, prefix[i] + suffix[i] + 1)

        return length - s

    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_lis(arr):
            stack, res = [], []
            for n in arr:
                index = bisect.bisect_left(stack, n)
                if index == len(stack):
                    stack.append(n)
                else:
                    stack[index] = n
                res.append(index)
            return res

        prefix, suffix = get_lis(nums), get_lis(nums[::-1])
        suffix.reverse()
        s, length = 3, len(nums)
        for i in range(1, length - 1):
            s = max(s, prefix[i] + suffix[i] + 1)

        return length - s
