import bisect


class Solution(object):
    def medianSlidingWindow_slow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        length = len(nums)
        arr = nums[:k-1]
        res = []
        for i in range(k-1, length):
            if i >= k:
                arr = arr[1:]
            arr.append(nums[i])
            sorted_arr = sorted(arr)
            if k % 2 :
                res.append(sorted_arr[k//2])
            else:
                res.append((sorted_arr[k//2-1] + sorted_arr[k//2])/2)
        return res

    def medianSlidingWindow(self, nums, k):
        odd = True if k % 2 else False
        half, arr, res = k//2, sorted(nums[:k-1]), []
        for i, val in enumerate(nums[k-1:]):
            arr.insert(bisect.bisect_left(arr, val), val)
            res.append(arr[half] if odd else (arr[half-1] + arr[half])/2)
            arr.pop(bisect.bisect_left(arr, nums[i]))
        return res