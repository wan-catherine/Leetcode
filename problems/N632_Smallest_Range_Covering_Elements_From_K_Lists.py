import bisect
import heapq
import sys

class Solution(object):
    def smallestRange_before(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        length = len(nums)
        arr = sorted([(li[0], i) for i, li in enumerate(nums)])
        lens = [len(li) for li in nums]
        indexes = [0] * length
        res = [arr[0][0], arr[-1][0]]
        while True:
            idx = 0
            while indexes[arr[idx][1]] == lens[arr[idx][1]] - 1:
                idx += 1
                if idx == length:
                    return res
            val, i = arr[idx]
            arr = arr[:idx] + arr[idx+1:]
            indexes[i] += 1
            bisect.insort_left(arr, (nums[i][indexes[i]], i))
            if arr[-1][0] - arr[0][0] < res[1] - res[0]:
                res = [arr[0][0], arr[-1][0]]

    """
    update at 20210130
    similar as 1675.
    """
    def smallestRange(self, nums):
        k = len(nums)
        arr = []
        index = [0] * k
        minimum, maximum = sys.maxsize, -sys.maxsize
        for i, li in enumerate(nums):
            arr.append((li[0], i))
            minimum = min(minimum, li[0])
            maximum = max(maximum, li[0])
        res = [minimum, maximum]
        heapq.heapify(arr)
        while True:
            val, idx = heapq.heappop(arr)
            if index[idx] + 1 == len(nums[idx]):
                break
            index[idx] += 1
            heapq.heappush(arr, (nums[idx][index[idx]], idx))
            minimum = arr[0][0]
            maximum = max(maximum, nums[idx][index[idx]])
            if maximum - minimum < res[1] - res[0]:
                res[0], res[1] = minimum, maximum
        return res