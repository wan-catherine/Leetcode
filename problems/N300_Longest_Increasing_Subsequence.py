import bisect


class Solution(object):
    def lengthOfLIS_before(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        status = []
        arr = []
        res = 0
        for i, n in enumerate(nums):
            index = bisect.bisect_left(arr, n)
            bisect.insort_left(arr, n)
            if index == 0:
                status.insert(index, 0)
            else:
                maximum = max(status[:index]) + 1
                status.insert(index, maximum)
                res = max(res, maximum)
        return res + 1

    """
    arr is the an array which is the longest increasing subsequence.
    when there is a new n , which is larger than arr[-1], then append it to arr .
    when there is a new n, whhich is smaller than arr[-1], find the smallest num in arr which larger than n. 
    then use n to replace this number . 
    This way, we can keep all numbers in array are as smaller as possble while keep the lenght same. 
    URL: https://www.youtube.com/watch?v=Q6KyDl_xiIg
    """
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        arr = []
        length = 0
        for i, n in enumerate(nums):
            index = bisect.bisect_left(arr, n)
            if index >= length:
                length += 1
                bisect.insort_left(arr, n)
            else:
                arr[index] = n
        return length
