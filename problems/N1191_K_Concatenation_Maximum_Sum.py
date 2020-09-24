"""
when arr's kadane value < 0, then it means all elements in the arr < 0, the res will be the empty arr : 0
when arr's kadane value == sum(arr), then it means all elements in the arr >= 0, the res will be the k*sum(arr)
when arr's kadane value > sum(arr), then we need to consider several different situations:
    1. arr's kadane  (the largest subset sum is in the middle of the arr
    2. two-arr's kadane (the largest subset sum is in the right of the arr added the left of the arr
    3. if sum(arr)>0, the aTTTTTb will be larger than ab(#2)
Return the largest one from 1,2,3.
"""
class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        arr_sum = sum(arr)
        one_arr = self.kadane(arr)
        if arr_sum == one_arr:
            return k*arr_sum%(10**9+7)
        if one_arr < 0:
            return 0
        two_arr = self.kadane(arr*2)
        if k > 2:
            res = max(one_arr, two_arr, two_arr+(k-2)*arr_sum)
        else:
            res = max(one_arr, two_arr)
        return res%(10**9+7)

    def kadane(self, arr):
        length = len(arr)
        current = arr[0]
        res = current
        for i in range(1, length):
            current = max(current + arr[i], arr[i])
            res = max(res, current)
        return res
