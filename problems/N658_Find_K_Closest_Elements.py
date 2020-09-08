import bisect
from math import inf


class Solution(object):
    def findClosestElements_my(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        length = len(arr)
        index = bisect.bisect_left(arr, x)
        res = []
        left, right = index - 1, index
        while k > 0:
            left_dis, right_dis = float(inf), float(inf)
            if left >= 0:
                left_dis = abs(x - arr[left])
            if right < length:
                right_dis = abs(x - arr[right])
            if left_dis <= right_dis:
                bisect.insort_left(res,arr[left])
                left -= 1
            else:
                bisect.insort_left(res,arr[right])
                right += 1
            k -= 1
        return res

    # Amazing solution
    def findClosestElements(self, A, k, x):
        left, right = 0, len(A) - k
        while left < right:
            mid = left + (right - left) // 2
            if x - A[mid] > A[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return A[left:left + k]