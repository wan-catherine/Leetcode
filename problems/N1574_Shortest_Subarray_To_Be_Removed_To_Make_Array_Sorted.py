from typing import List


class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = len(arr) - self.helper(arr)
        return res

    def helper(self, arr):
        if not arr:
            return 0
        cur = 0
        length = len(arr)
        if length == 1:
            return 1
        for left in range(length - 1):
            if arr[left] <= arr[left+1]:
                left += 1
            else:
                break
        if left == length - 1:
            return length
        for right in range(length-1, 0, -1):
            if arr[right] >= arr[right - 1]:
                right -= 1
            else:
                break
        cur = max(cur, left + 1, length - right)
        i,j = left, right
        while i >= 0:
            if arr[i] > arr[right]:
                i -= 1
            else:
                break
        cur = max(cur, i+1 + length - right)
        while j < length:
            if arr[j] < arr[left]:
                j += 1
            else:
                break
        cur = max(cur, left + 1 + length - j)

        i, j = left, right
        while i >= 0 and j < length:
            if arr[i] > arr[j]:
                i -= 1
            elif arr[i] < arr[j]:
                j += 1
            else:
                cur = max(cur, i + 1 + length - j)
                break
        return cur

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        length = len(arr)
        left, right = [arr[0]], [arr[-1]]
        i = 1
        while i < length and arr[i] >= left[-1]:
            left.append(arr[i])
            i += 1
        if i == length:
            return 0
        j = length - 2
        while j >= 0 and arr[j] <= right[-1]:
            right.append(arr[j])
            j -= 1
        right = right[::-1]

        ll, lr = len(left), len(right)
        res = max(ll, lr)
        i = ll - 1
        c = 0
        while i >= 0:
            idx = bisect.bisect_left(right, left[i])
            res = max(res, ll - c + lr - idx)
            c += 1
            i -= 1
        return length - res